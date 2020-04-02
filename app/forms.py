from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

# TODO: remove this flaskform
class EmailForm(FlaskForm):
    email = StringField('Email address', validators=[DataRequired(), Email()])
    submit = SubmitField('Send link')
