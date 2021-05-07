# from datetime import datetime
# from flaskapp import db, login_manager
# from flask_login import UserMixin


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     phone = db.Column(db.String(20), unique=False, nullable=True)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     profile = db.relationship('Profile', backref='author', lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"


# class Profile(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     content1 = db.Column(db.String(20), nullable=False) # Job Category
#     content2 = db.Column(db.String(20), nullable=False) # Major Category
#     content3 = db.Column(db.String(20), nullable=False) # Interest Category
#     content4 = db.Column(db.Text, nullable=False) # Current Project
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"

# @login_manager.user_loader
# def load_user(user_id):
#     return User_.query.get(int(user_id))


# class User_(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     birthdate = db.Column(db.DateTime)
#     cell_phone = db.Column(db.Integer)
#     profile = db.relationship('Profile', backref='author', lazy=True) #additional query in background
#     review = db.relationship('Review', backref='author', lazy=True) #additional query in background

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}')"

# class Profile(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
#     name = db.Column(db.String(20), unique=False, nullable=False)
#     age = db.Column(db.Integer)
#     school = db.Column(db.String(20))
#     user_id = db.Column(db.Integer, db.ForeignKey('user_.id'), nullable = False)

#     def __repr__(self):
#         return f"Profile('{self.name}')"

# class Review(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     stars = db.Column(db.Integer)
#     review_str = db.Column(db.Text)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user_.id'), nullable = False)
    
#     def __repr__(self):
#         return f"Review('{self.id}')"

# class Answer(db.Model):    
#     id = db.Column(db.Integer, primary_key=True)
#     field = db.Column(db.String(20), nullable=False)
#     major = db.Column(db.String(20), nullable=False)
#     interest = db.Column(db.String(20), nullable=False)
#     user_id = User_.query.order_by(User_.id.desc()).first()
    
#     def __repr__(self):
#         return f"Answer('{self.user_id}', '{self.field}','{self.major}','{self.interest}')"


# class Mentor_(db.Model):    
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), unique=False, nullable=False)
#     school = db.Column(db.String(20))
#     job_title = db.Column(db.String(20), nullable=False)
#     job_desc = db.Column(db.String(20))
#     image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
#     field = db.Column(db.String(20), nullable=False)
#     major = db.Column(db.String(20), nullable=False)
#     interest = db.Column(db.String(20), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
#     def __repr__(self):
#         return f"Answer('{self.user_id}', '{self.field}','{self.major}','{self.interest}')"


# For reference:

# class Post(db.Model): 
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"