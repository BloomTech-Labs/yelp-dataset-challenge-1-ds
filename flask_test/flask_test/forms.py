from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange

    
# adding review form class
class ReviewForm(FlaskForm):
    text = StringField('Review Text', 
                              validators = [DataRequired()])
    rating = IntegerField('Rating',
                                 validators = [DataRequired(), NumberRange(min=1, max=5, message="Please enter a whole number between 1 and 5.")])
    submit = SubmitField('Analyze Review Text')