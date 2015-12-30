from flask import Flask, jsonify, render_template, request, session
from models import db, Question, User, UserAnswer
from sqlalchemy.exc import IntegrityError
from flask.ext.cors import CORS

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
CORS(app)

@app.route("/")
def appSurvey():
    return render_template('app.html')

@app.route("/submit", methods=["POST"])
def submit():
    # validate name, email, birth date
    full_name = request.form.get("full_name", None)
    email = request.form.get("email", None)
    birth_date = request.form.get("birth_date", None)

    errors = []
    if full_name is None or not full_name:
        errors.append(dict(field="full_name",
                           message="Input Empty"))
    if email is None or not email:
        errors.append(dict(field="email",
                           message="Input Empty"))
    if birth_date is None or not birth_date:
        errors.append(dict(field="birth_date",
                           message="Input Empty"))    
    if len(errors) > 0:
        return json_respon(code=400,
                           msg="Input Empty",
                           errors=errors)
    
    # create new record in database
    user = User(full_name=full_name,
                email=email,
                birth_date=birth_date)
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        return json_respon(code=400,
                           msg=e.message)

    # save user information in session
    session["user_id"] = user.id
    data = dict(user=dict(id=user.id,
                          full_name=user.full_name,
                          email=user.email,
                          birth_date=user.birth_date))
    return json_respon(msg="User submitted successfully.",
                       data=data)

@app.route("/question")
def question_list():
    question = Question.query.all()

    data = []
    for q in question:
        data.append(dict(id=q.id,
                         text=q.text))
    return json_respon(data=data)

@app.route("/question/<int:id>", methods=["GET", "POST"])
def question(id):
    # check session
    if "user_id" not in session:
        return json_respon(code=400,
                           msg="You don't have any session to start answering question.")

    # fetch user
    user = User.query.get(session.get("user_id"))

    # fetch the question from the id,
    question = Question.query.get(id)
    # throw error if not found, redirect,
    # or just return an error message
    if question is None:
        return json_respon(404, "Question id: "+str(id)+" was not found.")

    question_data = dict(id=question.id,
                         text=question.text)

    # handle all post request
    if request.method == "POST":
        # check answer
        answer = request.form.get("answer", None)
        if answer is None:
            return json_respon(code=400,
                               msg="Answer Empty",
                               errors=dict(field="answer",
                                           message="Answer Empty"))

        # check if already answer
        if UserAnswer.query.filter_by(question=question,user=user).first():
            return json_respon(code=400,
                               msg="This question has been answered.")

        _user_answer = UserAnswer(user=user,
                        question=question,
                        answer=answer)
        try:
            db.session.add(_user_answer)
            db.session.commit()
        except:
            return json_respon(code=400,
                               msg="Answer cannot be craeted.")

        data = dict(user=dict(id=user.id,
                              full_name=user.full_name,
                              email=user.email,
                              birth_date=user.birth_date),
                    question=question_data,
                    user_answer=dict(id=_user_answer.id,
                                     user_id=_user_answer.user.id,
                                     question_id=_user_answer.question.id,
                                     answer=_user_answer.answer))
        return json_respon(code=201, data=data)

    # save how many question have been answered in session
    if "answer" in session: session["answer"] += 1
    else: session["answer"] = 1

    return json_respon(msg="Question No: " + str(id),
                       data=dict(question=question_data))

@app.route("/thanks")
def say_thanks():
    # check session
    # check session
    if "user_id" not in session:
        return json_respon(code=400,
                           msg="You don't have any session to start answering question.")

    # fetch user detail from session
    user = User.query.get(session.get("user_id"))
    data = dict(id=user.id,
                full_name=user.full_name,
                email=user.email,
                birth_date=user.birth_date)

    # destroy session
    session.pop("user_id")
    
    # return user data
    return json_respon(msg="Thank you.",
                       data=data)

@app.errorhandler(404)
def say_404(error):
    return json_respon(code=404, msg=error.description)

@app.errorhandler(500)
def say_500(error):
    return json_respon(code=500, msg=error.description)

# json response, don't repeat yourself :D
def json_respon(code=200, msg="OK", errors=None, data=None):
    _response = dict(code=code,
                     msg=msg)
    if errors: _response.update({'errors': errors})
    if data: _response.update({'data': data})
    return jsonify(_response), code