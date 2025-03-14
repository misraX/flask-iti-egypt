from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    """
    Our Agency Contact Form.
    """
    name = StringField('Name', validators=[DataRequired()], id='name')
    email = EmailField('Email', validators=[DataRequired()], id='mail')
    message = TextAreaField('Message', validators=[Length(min=5, max=10)], id='message')
