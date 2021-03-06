# from flask_wtf import FlaskForm
# from flask_login import current_user
# from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, FileField
# from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# from flaskapp.models import User_


# class RegistrationForm(FlaskForm):
#     username = StringField('Username',
#                            validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password',
#                                      validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')

#     def validate_username(self, username):
#         if username.data != current_user.username:
#             user = User_.query.filter_by(username=username.data).first()
#             if user:
#                 raise ValidationError('That username is taken. Please choose a different one.')

#     def validate_email(self, email):
#         if email.data != current_user.email:
#             user = User_.query.filter_by(email=email.data).first()
#             if user:
#                 raise ValidationError('That email is taken. Please choose a different one.')



# class UpdateAccountForm(FlaskForm):
#     username = StringField('Username',
#                            validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password',
#                                      validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Update_')

#     def validate_username(self, username):

#         user = User_.query.filter_by(username=username.data).first()

#         if user:
#             raise ValidationError('That username already exists.')

#     def validate_email(self, email):

#         user = User_.query.filter_by(email=email.data).first()

#         if user:
#             raise ValidationError('That email already exists.')



# class LoginForm(FlaskForm):
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')


# class InfoForm(FlaskForm):
#     picture = FileField('Update Profile Picture')
#     name = StringField('Name', validators=[DataRequired()])
#     age = IntegerField('Age', validators=[DataRequired()])
#     cell_phone = StringField('Cell Phone', validators=[DataRequired()])
#     school = StringField('School or Work', validators=[DataRequired()])

#     submit = SubmitField('Continue')

#     # title = StringField('Title', validators=[DataRequired()])
#     # content = TextAreaField('Content', validators=[DataRequired()])
#     # submit = SubmitField('Post')
