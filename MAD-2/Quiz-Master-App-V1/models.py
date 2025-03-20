import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()


class Role(db.Model, RoleMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True) 

  users = db.relationship('User', backref='role')


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(150), unique=True, nullable=False)
  pwd = db.Column(db.String(255), nullable=False)
  dob = db.Column(db.String, nullable=False)  
  role_id = db.Column(db.Integer, db.ForeignKey('role.id'), default=1)
  # flask-security related
  active = db.Column(db.Boolean, default=True)
  fs_uniquifier = db.Column(db.String, unique=True, default=lambda: str(uuid.uuid4()))

  attempts = db.relationship('QuizAttempt', backref='user', cascade="all, delete", lazy=True)


class Subject(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True, nullable=False)
  description = db.Column(db.Text, nullable=True)
  
  chapters = db.relationship('Chapter', backref='subject', cascade="all, delete", lazy=True)

class Chapter(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.Text, nullable=True)
  subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)

  questions = db.relationship('Question', backref='chapter', cascade="all, delete", lazy=True)
  quizzes = db.relationship('Quiz', backref='chapter', cascade="all, delete", lazy=True)

class Question(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'), nullable=False)
  question_text = db.Column(db.Text, nullable=False)
  
  option_1 = db.Column(db.String(255), nullable=False)
  option_2 = db.Column(db.String(255), nullable=False)
  option_3 = db.Column(db.String(255), nullable=False)
  option_4 = db.Column(db.String(255), nullable=False)
  correct_option = db.Column(db.Integer, nullable=False)  # Stores 1,2,3,4 as correct answer index

  quizzes = db.relationship('QuizQuestion', backref='question', cascade="all, delete", lazy=True)

class Quiz(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'), nullable=False)
  date = db.Column(db.Date, nullable=False)
  duration = db.Column(db.Integer, nullable=False)  # Duration in minutes
  
  questions = db.relationship('QuizQuestion', backref='quiz', cascade="all, delete", lazy=True)
  attempts = db.relationship('QuizAttempt', backref='quiz', cascade="all, delete", lazy=True)

class QuizQuestion(db.Model):  # Many-to-Many Relationship Between Quiz & Questions
  id = db.Column(db.Integer, primary_key=True)
  quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
  question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)

class QuizAttempt(db.Model):  # Tracks user attempts
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
  score = db.Column(db.Integer, nullable=True)  # Nullable initially, set after submission
  completed = db.Column(db.Boolean, default=False)

  responses = db.relationship('UserResponse', backref='attempt', cascade="all, delete", lazy=True)


class UserResponse(db.Model):  # Stores user's selected answers
  id = db.Column(db.Integer, primary_key=True)
  attempt_id = db.Column(db.Integer, db.ForeignKey('quiz_attempt.id'), nullable=False)
  question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
  selected_option = db.Column(db.Integer, nullable=False)  # Stores 1,2,3,4 as selected option
