from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange

# adding registration form class
# class RegistrationForm(FlaskForm):
#     username = StringField('Username', 
#                            validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField('Email',
#                         validators = [DataRequired(), Email()])
#     password = PasswordField('Password', 
#                              validators = [DataRequired()])
#     confirm_password = PasswordField('Confirm Password', 
#                              validators = [DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')

# adding login form class
# class LoginForm(FlaskForm):
#     email = StringField('Email',
#                         validators = [DataRequired(), Email()])
#     password = PasswordField('Password', 
#                              validators = [DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')
    
# adding review form class
class ReviewForm(FlaskForm):
    review_text = StringField('Review Text', 
                              validators = [DataRequired()])
    review_rating = IntegerField('Rating',
                                 validators = [DataRequired(), NumberRange(min=1, max=5, message="Please enter a whole number between 1 and 5.")])
    submit = SubmitField('Analyze Review Text')