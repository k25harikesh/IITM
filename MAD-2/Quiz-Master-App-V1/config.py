from models import db, Role


class Config():
  DEBUG = True
  SECRET_KEY = 'super secret key'
  SECURITY_PASSWORD_SALT = 'secret salt'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///Quiz-data.sqlite3'
  SQLALCHEMY_TRACK_MODIFICATIONS = False  

  WTF_CSRF_ENABLED = False

def seed_roles():
  if not Role.query.first():  # Insert only if no roles exist
    admin_role = Role(id=0, name="Admin")
    user_role = Role(id=1, name="User")
    db.session.add_all([admin_role, user_role])
    db.session.commit()
