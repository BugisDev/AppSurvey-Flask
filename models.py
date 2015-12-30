from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from _ast import TryExcept

db = SQLAlchemy()

class User(db.Model):
    """
    Set Table Name
    """
    __tablename__ = "app_user"
    
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120))
    email = db.Column(db.String(80), unique=True)
    birth_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    def __init__(self, full_name, email, birth_date):
        self.created_at = datetime.now()
        self.full_name = full_name
        self.email = email
        self.birth_date = birth_date
    
    def __repr__(self):
        return '<User {}>'.format(self.full_name)

class Question(db.Model):
    """
    Set Table Name
    """
    __tablename__ = "app_question"
    
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    def __init__(self, text):
        self.created_at = datetime.now()
        self.text = text
    
    def __repr__(self):
        return '<Question {}>'.format(self.id)
    
class UserAnswer(db.Model):
    """
    Set Table Name
    """
    __tablename__ = "app_user_answer"
    
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('app_user.id'))
    user = db.relationship('User',
                           backref=db.backref('answers', lazy='dynamic'))
    question_id = db.Column(db.Integer, db.ForeignKey('app_question.id'))
    question = db.relationship('Question',
                           backref=db.backref('answers', lazy='dynamic'))
    answer = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)
 
    def __init__(self, user, question, answer):
        self.created_at = datetime.now()
        self.user = user
        self.question = question
        self.answer = answer
    
    def __repr__(self):
        return '<UserAnswer {}>'.format(self.answer)