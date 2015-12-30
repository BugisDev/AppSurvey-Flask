from flask import Flask, jsonify, render_template, request, session
from models import db, Question, User, UserAnswer

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

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
    if full_name is None:
        errors.append(dict(field="full_name",
                           message="Input Empty"))
    if email is None:
        errors.append(dict(field="email",
                           message="Input Empty"))
    
    if birth_date is None:
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
    db.session.add(user)
    db.session.commit()

    # save user information in session
    session["user_id"] = user.id
    return json_respon(msg="User submitted successfully.",
                       data=dict(user=dict(id=user.id,
                                           full_name=user.full_name,
                                           email=user.email,
                                           birth_date=user.birth_date)))

@app.route("/question/<int:id>", methods=["GET", "POST"])
def question(id):
    # check session
    if "user_id" not in session:
        return json_respon(code=400,
                           msg="You don't have any session to start answering question.")

    # handle all post request
    if request.method == "POST":
        return json_respon(msg="OK")

    # do the rest here, include get request
    
    # fetch the question from the id,
    # throw error if not found, redirect,
    # or just return an error message
    
    return json_respon(msg="OK")

@app.route("/thanks")
def say_thanks():
    # check session
    
    # fetch user detail from session

    # destroy session

    return json_respon(msg="OK")

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
    if errors: _response.update({errors: errors})
    if data: _response.update({data: data})
    return jsonify(_response), code

if __name__ == "__main__":
    app.run(debug=True)