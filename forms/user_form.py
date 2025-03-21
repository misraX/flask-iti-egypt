from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, EmailField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    """
    Our Agency Contact Form.
    """
    first_name = StringField('First Name', validators=[DataRequired()], id='first_name')
    last_name = StringField('Last Name', validators=[DataRequired()], id='last_name')
    email = EmailField('Email', validators=[DataRequired()], id='email')
    country = StringField('Country', validators=[DataRequired()], id='country')
