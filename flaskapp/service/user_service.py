import uuid
import datetime

from flaskapp import db
from flaskapp.model.user import User

def save_new_user(data):
  email = data['email']
  username = data['username'],
  password = data['password'],
  birthdate = data['birthdate']
  cell = data['cell_phone']

  # TODO validate email/password

  user = User.query.filter_by(email=email).first()
  if user:
    return False, "User already exists"
  
  new_user = User(
    email=email,
    username=username,
    password=password,
    birthdate=birthdate,
    cell_phone=cell,
    registered_on=datetime.datetime.utcnow()
  )
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

