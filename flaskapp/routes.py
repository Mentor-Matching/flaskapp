# import secrets
# import os
from flask import render_template, url_for, flash, redirect, request

# from flaskapp import app, db, bcrypt
# from flaskapp.forms import RegistrationForm, LoginForm, InfoForm
# from flaskapp.models import User_, Profile, Review
# from flask_login import login_user, current_user, logout_user, login_required

from flask import request
from flaskapp import app, db
from flaskapp.model.user import USER_TYPE_MENTOR, USER_TYPE_MENTEE
from flaskapp.service.user_service import save_new_user, get_user
from flaskapp.service.matching_service import perform_matching
import pandas as pd
import os



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

@app.route('/sign-up/basic-info', methods=['GET'])
def basicInfo():
  return render_template('index.html')
@app.route('/sign-up/interests', methods=['GET'])
def interests():
  return render_template('index.html')
@app.route('/profile/mentee', methods=['GET'])
def menteeProfile():
  return render_template('index.html')




  
'''
Landing page  
'''
# Sample Data
mentor = [
    {
        'name': '서달미',
        'title': '삼산텍 CEO',
        'job_content': '채용, 투자유치, IR등'
    },
    {
        'name': '남도산',
        'title': '삼산텍 CTO',
        'job_content': '기술 및 개발 총괄 리드'
    }
]

@app.route('/api/recommendations/sample', methods=['GET'])
def landing():

  return render_template('landing.html', mentor=mentor)




'''
Sign up page
'''

@app.route("/api/profile/registration", methods=[ 'GET','POST'])
def registration():
    if current_user.is_authenticated:
        return 'Already Logged In' #redirect(url_for('home'))
    form = RegistrationForm()
    form.validate_username(form.username)
    form.validate_email(form.email)
    if form.validate_on_submit(): #need to change this to validate_on_submit...
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User_(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'Your Account has been created!', 'success')
        return redirect(url_for('info'))
    
    return render_template('register.html', title='Register', form=form)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route("/api/profile/info", methods=[ 'GET','POST'])
def info():
    
    form = InfoForm()
    if form.submit(): #need to change this to validate_on_submit...
      if form.picture.data:
        a=1
      else:
        return render_template('info.html', title='Register', form=form)
      image_file = save_picture(form.picture.data)
      user_id = User_.query.order_by(User_.id.desc()).first() #bring the last added user
      profile = Profile(image_file = form.image_file.data, name = form.name.data, age = form.age.data,
      cell_phone = form.cell_phone.data, school = form.school.data, user_id = user_id)
      db.session.add(profile)
      db.session.commit()

      return redirect(url_for('login'))
  
    return render_template('info.html', title='Register', form=form)

'''
Account Page
'''

@app.route("/account", methods=['GET'])
def account():
  filename = 'profile_pics/profile.png'
  return render_template('account.html', title='Account', filename=filename)


'''
Recommendation page
'''
@app.route('/api/recommendations', methods=['GET']) # TODO: Use session to avoid exposing userId/info
def api_reviews():
  # TODO: user ID 110 is the ONLY Mentee right now.
  user_id = request.args.get('user_id')
  user = get_user(int(user_id))
  if not user:
    return "INVALID USER", 400

  mentor_ids = perform_matching(user)

  return str(mentor_ids), 200


'''
Login Page: Only For Development Purpose
'''

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template('logged_in.html', title='Logged_In')
    form = LoginForm()
    if form.validate_on_submit():
        user = User_.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(url_for('landing')) 
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return  render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login')) 



'''
Testing endpoint
'''

# This endpoint will create all DB tables for which models exist
@app.route('/internal/createModelTables', methods=['GET'])
def createTableBasedOnModel():
  db.create_all()
  db.session.commit()
  return "SUCCESES??", 200

# This will bulk upload the csv (local) file into DB
@app.route('/internal/mentors/upload', methods=['GET'])
def bulkUploadMentors():
  path = os.path.dirname(os.path.realpath(__file__))
  mentors = pd.read_csv('{}/matchmaker/mentors_updated.csv'.format(path))
  mentors_dict = mentors.to_dict(orient='records')
  with db.session.begin():
    for mentor in mentors_dict:
      res, message = save_new_user(mentor, USER_TYPE_MENTOR, transaction=True)
      print("USER {}: {}".format(mentor['name'], message))

  return "Success!", 200


# Manually create mentee by modifying below and making a request to this endpoint
@app.route('/internal/mentee/', methods=['GET'])
def createMentee():
  user = {
    "email": "koohakwo126@mentormatching.com",
    "username": "koohakwo",
    "password": "MentorMatchingDemo!",
    "birthdate": "4/24/1993",
    "cell_phone": 2067797250,
    "field": "['방송', '마케팅','디자인']",
    "major": "[''공연예술과', '공업디자인']",
    "interest": "['우주', '게임','미술']",
    "hobby" : "저는 거의 매일 영화를 봅니다. 유투브 자주 보는것 같습니다. 여러 매체의 영상들을 작업하는 것을 좋아합니다",
    "project": "저는 학교 프로젝트로 고등학생들을 여러 문제점들을 파해치는 다큐멘터리를 만들고 있습니다. 전에도 몇번 짧은 영상들을 만들어 보았지만 이렇게 긴 영상을 만드는 것은 처음입니다. 이 부분을 도와주세요."
  }
  res, message = save_new_user(user, USER_TYPE_MENTEE)
  if not res:
    return "ERROR: {}".format(message), 400
  return "SUCCESS", 200


@app.route('/test', methods=['GET'])
def test():
  return 'it works!'


'''
Page Not Found
'''
