from flask import render_template, url_for, redirect, request, flash
from flask_security import login_user, logout_user, auth_required, SQLAlchemyUserDatastore, current_user
from flask_security.utils import verify_password
from flask import current_app as app
from datetime import datetime
from models import *

# datastore: SQLAlchemyUserDatastore = app.security.datastore

@app.get('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    uname = request.form.get("username")
    pwd = request.form.get("password")
    usr = User.query.filter_by(email=uname).first()
    
    if usr and verify_password(pwd, usr.pwd):
      login_user(usr)
      flash("Login successful!", "success")
      if usr.role_id == 0:
        return redirect(url_for('dashboard'))
      return redirect(url_for('user_dashboard'))
    
    flash("Invalid credentials, please try again.", "danger")
  
  return render_template('auth/login.html')

@app.get('/logout')
def logout():
  logout_user()
  flash("Logged out successfully!", "info")
  return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    email = request.form.get("email")
    pwd = request.form.get("pwd")
    name = request.form.get("name")
    dob = request.form.get("dob")

    if User.query.filter_by(email=email).first():
      flash("Email already exists.", "danger")
      return redirect(url_for('register'))
  
    new_user = User(email=email, pwd=pwd, name=name, dob=datetime.strptime(dob, '%Y-%m-%d'))
    db.session.add(new_user)
    db.session.commit()

    flash("Registration successful!", "success")
    return redirect(url_for('login'))

  return render_template('auth/register.html')


@app.route('/dashboard')
@auth_required()
def dashboard():
  if current_user.role_id != 0:
    flash("Unauthorized access!", "danger")
    return redirect(url_for('user_dashboard'))
  
  subjects = Subject.query.all()
  return render_template('admin/admin_dashboard.html', subjects=subjects)

@app.route('/add_subject', methods=['GET', 'POST'])
@auth_required()
def add_subject():
  if request.method == 'POST':
    name = request.form.get("name")
    description = request.form.get("description")

    if not name:
      flash("Subject name is required", "danger")
      return render_template('admin/new_subject.html')

    if Subject.query.filter_by(name=name).first():
      flash("Subject already exists", "danger")
      return render_template('admin/new_subject.html')

    new_subject = Subject(name=name, description=description)
    db.session.add(new_subject)
    db.session.commit()
    return redirect(url_for('dashboard'))

  return render_template('admin/new_subject.html')

@app.route('/edit_subject/<int:subject_id>', methods=['GET', 'POST'])
@auth_required()
def edit_subject(subject_id):
  subject = Subject.query.get_or_404(subject_id)
  
  if request.method == 'POST':
    subject.name = request.form.get("name")
    subject.description = request.form.get("description")
    db.session.commit()
    flash("Subject updated successfully!", "success")
    return redirect(url_for('dashboard'))
  
  return render_template('admin/new_subject.html', subject=subject)

@app.route('/delete_subject/<int:subject_id>')
@auth_required()
def delete_subject(subject_id):
  subject = Subject.query.get_or_404(subject_id)
  db.session.delete(subject)
  db.session.commit()
  flash("Subject deleted successfully!", "danger")
  return redirect(url_for('dashboard'))

# Chapters

@app.route('/add_chapter/<string:subject_name>', methods=['GET', 'POST'])
@auth_required()
def add_chapter(subject_name):
  subject = Subject.query.filter_by(name=subject_name).first()
  if not subject:
    return "Subject not found", 404

  if request.method == 'POST':
    name = request.form.get("name")
    description = request.form.get("description")

    if not name:
      return render_template('admin/new_chapter.html', subject=subject, error="Chapter name is required")
    
    new_chapter = Chapter(name=name, description=description, subject_id=subject.id)
    db.session.add(new_chapter)
    db.session.commit()
    return redirect(url_for('dashboard'))

  return render_template('admin/new_chapter.html', subject=subject)

@app.route('/edit_chapter/<int:chapter_id>', methods=['GET', 'POST'])
@auth_required()
def edit_chapter(chapter_id):
  chapter = Chapter.query.get_or_404(chapter_id)

  if request.method == 'POST':
    chapter.name = request.form.get("name")
    chapter.description = request.form.get("description")
    db.session.commit()
    flash("Chapter updated successfully!", "success")
    return redirect(url_for('dashboard'))

  return render_template('admin/new_chapter.html', chapter=chapter)

@app.route('/delete_chapter/<int:chapter_id>', methods=['GET'])
@auth_required()
def delete_chapter(chapter_id):
  chapter = Chapter.query.get_or_404(chapter_id)
  db.session.delete(chapter)
  db.session.commit()
  flash("Chapter deleted successfully!", "success")
  return redirect(url_for('dashboard'))

# Quiz

@app.get('/quiz')
@auth_required()
def quiz():
  quizzes = Quiz.query.all()
  return render_template('admin/quiz_management.html', quizzes=quizzes)

@app.route('/add_quiz', methods=['GET', 'POST'])
@auth_required()
def add_quiz():
  if request.method == 'POST':
    chapter_name = request.form.get("chapter_name")
    date = request.form.get("date")
    duration = request.form.get("duration")
    
    chapter = Chapter.query.filter_by(name=chapter_name).first()
    if not chapter:
      flash("Chapter not found. Please enter a valid chapter name.", "danger")
      return redirect(url_for('add_quiz'))
    
    new_quiz = Quiz(
      chapter_id=chapter.id,
      date=datetime.strptime(date, '%Y-%m-%d'),
      duration=int(duration)
    )
    db.session.add(new_quiz)
    db.session.commit()
    flash("Quiz created successfully!", "success")
    return redirect(url_for('quiz'))

  return render_template('admin/new_quiz.html')

@app.route('/quiz/<int:quiz_id>/edit', methods=['GET', 'POST'])
@auth_required()
def edit_quiz(quiz_id):
  quiz = Quiz.query.get_or_404(quiz_id)

  if request.method == 'POST':
    quiz.date = datetime.strptime(request.form.get("date"), '%Y-%m-%d')
    quiz.duration = int(request.form.get("duration"))
    db.session.commit()
    flash("Quiz updated successfully!", "success")
    return redirect(url_for('quiz'))

  return render_template('admin/new_quiz.html', quiz=quiz)

@app.route('/delete_quiz/<int:quiz_id>', methods=['POST'])
@auth_required()
def delete_quiz(quiz_id):
  quiz = Quiz.query.get_or_404(quiz_id)
  db.session.delete(quiz)
  db.session.commit()
  flash("Quiz deleted successfully!", "success")
  return redirect(url_for('quiz'))

# Questions

@app.route('/add_question/<quiz_id>', methods=['GET', 'POST'])
@auth_required()
def add_question(quiz_id):
  quiz = Quiz.query.get_or_404(quiz_id)
  chapter_id = quiz.chapter_id  # chapter_id from quiz
  
  if request.method == 'POST':
    question_text = request.form.get("question_text")
    option_1 = request.form.get("option_1")
    option_2 = request.form.get("option_2")
    option_3 = request.form.get("option_3")
    option_4 = request.form.get("option_4")
    correct_option = request.form.get("correct_option")

    new_question = Question(      
      chapter_id=chapter_id,
      question_text=question_text,
      option_1=option_1,
      option_2=option_2,
      option_3=option_3,
      option_4=option_4,
      correct_option=int(correct_option)
    )
    db.session.add(new_question)
    db.session.commit()

    # Add Question to Quiz
    quiz_question = QuizQuestion(quiz_id=quiz.id, question_id=new_question.id)
    db.session.add(quiz_question)
    db.session.commit()
    return redirect(url_for('quiz'))
    
  return render_template('admin/new_question.html', quiz=quiz, chapter_id=chapter_id)

@app.route('/edit_question/<int:question_id>', methods=['GET', 'POST'])
@auth_required()
def edit_question(question_id):
  question = Question.query.get_or_404(question_id)
  
  if request.method == 'POST':
    question.question_text = request.form.get("question_text")
    question.option_1 = request.form.get("option_1")
    question.option_2 = request.form.get("option_2")
    question.option_3 = request.form.get("option_3")
    question.option_4 = request.form.get("option_4")
    question.correct_option = int(request.form.get("correct_option"))
    db.session.commit()
    flash("Question updated successfully!", "success")
    return redirect(url_for('quiz'))
  
  return render_template('admin/new_question.html', question=question)

@app.route('/delete_question/<int:question_id>', methods=['POST', 'GET'])
@auth_required()
def delete_question(question_id):
  question = Question.query.get_or_404(question_id)
  db.session.delete(question)
  db.session.commit()
  flash("Question deleted successfully!", "success")
  return redirect(url_for('quiz'))

@app.get('/summary')
@auth_required()
def summary():
  return render_template('admin/summary.html')

# User Routes

@app.route('/user_dashboard')
@auth_required()
def user_dashboard():
  quizzes = Quiz.query.all()
  return render_template('user/user_dashboard.html', quizzes=quizzes)

@app.route('/user/quiz/<int:quiz_id>')
@auth_required()
def view_quiz(quiz_id):
  quiz = Quiz.query.get_or_404(quiz_id)
  return render_template('user/view_quiz.html', quiz=quiz)

@app.route('/user/quiz/start/<int:quiz_id>')
@auth_required()
def start_quiz(quiz_id):
  quiz = Quiz.query.get_or_404(quiz_id)
  attempt = QuizAttempt.query.filter_by(user_id=current_user.id, quiz_id=quiz_id).first()
  
  if attempt and attempt.completed:
    flash("You have already completed this quiz.", "warning")
    return redirect(url_for('user_score'))

  return render_template('user/start_quiz.html', quiz=quiz)

@app.route('/user/quiz/submit/<int:quiz_id>', methods=['POST'])
@auth_required()
def submit_quiz(quiz_id):
  quiz = Quiz.query.get_or_404(quiz_id)
  attempt = QuizAttempt.query.filter_by(user_id=current_user.id, quiz_id=quiz_id).first()

  if attempt and attempt.completed:
    flash("You have already submitted this quiz.", "warning")
    return redirect(url_for('user_score'))

  if not attempt:
    attempt = QuizAttempt(user_id=current_user.id, quiz_id=quiz_id, score=0, completed=False)
    db.session.add(attempt)

  score = 0
  for quiz_question in quiz.questions:
    question = quiz_question.question
    user_answer = request.form.get(f'q{question.id}', None)
    
    if user_answer and int(user_answer) == question.correct_option:
      score += 1
      # saving User Response
      response = UserResponse(
        attempt_id=attempt.id,
        question_id=question.id,
        selected_option=user_answer
      )
      db.session.add(response)

  attempt.score = score
  attempt.completed = True
  db.session.commit()

  flash(f"Quiz submitted! Your score: {score}/{len(quiz.questions)}", "success")
  return redirect(url_for('user_score'))

@app.get('/user_summary')
@auth_required()
def user_summary():
  return render_template('user/user_summary.html')

@app.get('/user_score')
@auth_required()
def user_score():
  attempt = QuizAttempt.query.filter_by(user_id=current_user.id).all()
  return render_template('user/score.html', attempts=attempt)
