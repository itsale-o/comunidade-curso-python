from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e18e9c53ca9294cea12aae49b35cbed3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:MurZLbTbMVJk8avlRpFG@containers-us-west-68.railway.app:6644/railway'

if os.getenv("DATABASE_URL"):
  app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeimpresionadora import routes

