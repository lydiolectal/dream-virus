from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class DreamForm(FlaskForm):
    # record email
    submit = SubmitField('Send link')
