from flaskapp import db

USER_TYPE_UNKNOWN = 0
USER_TYPE_MENTOR = 1
USER_TYPE_MENTEE = 2


class User(db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)
  birthdate = db.Column(db.DateTime)
  cell_phone = db.Column(db.Integer)
  registered_on = db.Column(db.DateTime)
  type = db.Column(db.Integer, nullable=False)

  __mapper_args__ = {
    'polymorphic_on': type,
    'polymorphic_identity': USER_TYPE_UNKNOWN
  }

  def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}

  def __repr__(self):
      return f"User('{self.username}', '{self.email}')"


class Mentor(User):
  __tablename__ = 'mentor'
  id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
  school = db.Column(db.String(20))
  job_title = db.Column(db.String(20), nullable=False)
  job_desc = db.Column(db.String(20))
  image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
  field = db.Column(db.String(20), nullable=False)
  major = db.Column(db.String(20), nullable=False)
  interest = db.Column(db.String(20), nullable=False)

  __mapper_args__ = {
    'polymorphic_identity': USER_TYPE_MENTOR
  }

  def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Mentee(User):
  __tablename__ = 'mentee'
  id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
  field = db.Column(db.String(20), nullable=False)
  major = db.Column(db.String(20), nullable=False)
  interest = db.Column(db.String(20), nullable=False)

  __mapper_args__ = {
    'polymorphic_identity': USER_TYPE_MENTEE
  }

  def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}
