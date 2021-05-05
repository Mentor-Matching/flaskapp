from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'mango213diojfeklvkl34l234l' #kk
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/flaskapp' #'sqlite:///site.db' #kk

db = SQLAlchemy(app) #kk
bcrypt = Bcrypt(app) #kk
login_manager = LoginManager(app) #kk
login_manager.login_view = 'login' #kk

from flaskapp import routes