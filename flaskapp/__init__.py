# from flask import Flask, render_template, send_from_directory
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager

# import os
# import pyodbc
# import sqlalchemy as sa
# from sqlalchemy import create_engine
# from urllib.parse import quote_plus 



# app = Flask(__name__, static_url_path='')

# # Configure Database URI: 
# params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=sqlhost.database.windows.net;DATABASE=pythonSQL;UID=username@sqldb;PWD=password56789")


# app.config['SECRET_KEY'] = 'mango213diojfeklvkl34l234l' #kk
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #kk

# "mssql+pyodbc:///?odbc_connect=%s"
#'postgresql://postgres:test123@localhost/flaskapp' #'sqlite:///site.db' #kk

# db = SQLAlchemy(app) #kk
# bcrypt = Bcrypt(app) #kk
# login_manager = LoginManager(app) #kk
# login_manager.login_view = 'login' #kk




################ PROD SETTINGS #################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, static_url_path='')
# TODO: Make this stuff environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mmDev@mm-mariadb-dev:MentorMatching!@mm-mariadb-dev.mariadb.database.azure.com/MentorMatching'
db = SQLAlchemy(app)
# bcrypt = Bcrypt(app) #kk
# login_manager = LoginManager(app) #kk
# login_manager.login_view = 'login' #kk

################################################



from flaskapp import routes