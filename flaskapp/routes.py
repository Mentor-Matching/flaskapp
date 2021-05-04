from app import app
from flask import render_template, url_for, flash, redirect, request
from flaskapp import app, db, bcrypt
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


'''
Page rendering
'''

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/sign-up', methods=['GET'])
def signUp():
  return render_template('index.html')

@app.route('/calendar', methods=['GET'])
def calendar():
  return render_template('index.html')

@app.route('/reviews', methods=['GET'])
def reviews():
  return render_template('index.html')

'''
Landing page
'''



'''
Sign up page
'''
@app.route("/registration", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'Your Account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('index.html', title='Registeration', form=form) # This needs to be updated


'''
Recommendation page
'''
@app.route('/reviews', methods=['GET']) #Kooha
def reviews():
  return render_template('index.html')


'''
Testing endpoint
'''

@app.route('/test', methods=['GET'])
def test():
  return 'it works!'

'''
Page Not Found
'''

# @app.errorhandler(404)
# def pageNotFound(e):
#   return render_template('index.html')