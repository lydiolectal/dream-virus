from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Regexp

class DreamForm(FlaskForm):
    # initials must be alpha characters only
    initials = StringField('Initials', validators=[InputRequired(), Regexp("[a-zA-Z]+")])
    # location must be country or city, validated against google places api
    location = StringField('Location', validators=[InputRequired()])
    # dream_date must follow Y-M-D format
    dream_date = DateField('Date of dream', validators=[InputRequired()], format='%m/%d/%Y') 
    dream_text = StringField('Dream', validators=[InputRequired()])
    tags = BooleanField('Tags')
    content_warnings = BooleanField('Content warnings') 
    # agree_to_copyright must be checked; DataRequired checks that input is 'truthy'
    agree_to_copyright = BooleanField('C.C. 4.0', validators=[DataRequired()])
    submit = SubmitField('Submit')
