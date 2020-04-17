from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, StringField, SubmitField
from wtforms.fields import SelectMultipleField
from wtforms.validators import DataRequired, InputRequired, Regexp, Length
from wtforms.widgets import TextArea, ListWidget, CheckboxInput

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class DreamForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(max=128)])
    # name must be alpha characters only
    name = StringField('Name', validators=[InputRequired(), Regexp("[a-zA-Z]+"), Length(max=64)])
    # location must be country or city, validated against google places api
    location = StringField('Location', validators=[InputRequired(), Length(max=64)])
    # dream_date must follow Y-M-D format
    date = DateField('Date of dream', validators=[InputRequired()], format='%m/%d/%Y') 
    content = StringField('Dream', widget=TextArea(), validators=[InputRequired()])
    # TODO: populate with query results from 'themes' db table instead
    themes = MultiCheckboxField(
        'Themes',
        choices=[(1, 'Falling'), (2, 'Being chased'), (3, 'Nakedness')]
    )
    content_warnings = MultiCheckboxField(
        'Content Warnings',
        choices=[(1, 'Physical violence'), (2, 'Death'), (3, 'Mental illness')]
    )
    # agree_to_copyright must be checked; DataRequired checks that input is 'truthy'
    agree_to_copyright = BooleanField('I agree', validators=[DataRequired()])
    submit = SubmitField('Submit')
