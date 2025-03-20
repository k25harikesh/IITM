from flask import Flask, redirect, url_for
from config import Config, seed_roles
from models import db, User, Role
from flask_security import Security, SQLAlchemyUserDatastore


def set_up():
  app = Flask(__name__)
  app.config.from_object(Config)

  # db set_up
  db.init_app(app)

  # flask-Security set_up
  datastore = SQLAlchemyUserDatastore(db, User, Role)
  app.security = Security(app, datastore=datastore, register_blueprint=False)

  # pushing application context
  app.app_context().push()
  print('App started ... ')

  # checks if !instance then run
  db.create_all()

  return app

app = set_up()
seed_roles()

import routes

if __name__ == '__main__':
  app.run(debug=True)