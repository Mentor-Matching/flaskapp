import uuid
import datetime
import math

from flaskapp import db
from flaskapp.model.user import User, Mentor, Mentee, USER_TYPE_MENTEE, USER_TYPE_MENTOR

def save_new_user(data, userType, transaction=False):
  if not data or userType not in [USER_TYPE_MENTEE, USER_TYPE_MENTOR]:
    return False, "Invalid arguments"

  if not data['field'] or not data['major'] or not data['interest']:
    return False, "Invalid arguments"

  email = data['email']
  username = data['username'],
  password = data['password'],
  birthdate = None
  cell = 0

  user = User.query.filter_by(email=email).first()
  if user:
    return False, "User already exists"
  
  if userType == USER_TYPE_MENTEE:
    new_user = Mentee(
      email=email,
      username=username,
      password=password,
      birthdate=birthdate,
      cell_phone=cell,
      registered_on=datetime.datetime.utcnow(),
      field=data['field'],
      major=data['major'],
      interest=data['interest'],
      hobby=data['hobby'],
      project=data['project']
    )
  elif userType == USER_TYPE_MENTOR:
    if not data['job_title']:
      return False, "Invalid arguments"
    if type(data['job_desc']) is not str and math.isnan(data['job_desc']):
      return False, "job_desc is NaN"
    new_user = Mentor(
      email=email,
      username=username,
      password=password,
      birthdate=birthdate,
      cell_phone=cell,
      registered_on=datetime.datetime.utcnow(),
      school=data['school'],
      job_title=data['job_title'],
      job_desc=data['job_desc'],
      image_file=data['image_file'],
      field=data['field'],
      major=data['major'],
      interest=data['interest']
    )
  else:
    return False, "Invalid arguments"

  if transaction:
    db.session.add(new_user)
    return True, "[TRANSACTION] Successfully saved new user"

  db.session.add(new_user)
  db.session.commit()
  return True, "Successfully saved new user"


def get_user(id):
  if not id or not isinstance(id, int):
    return None
  user = User.query.get(id)
  print(user)
  # TODO: Authentication
  return user

def get_all_mentors():
  return Mentor.query.all()
