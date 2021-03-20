from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Email, DataRequired, ValidationError

class MessageForm(FlaskForm):
    def validate_email(self, email_to_check):
        email = str(email_to_check)
        if not "@" in email:
            return ValidationError('Entered email is of wrong format')    
    name    =   StringField(label='You name', validators=[DataRequired()])
    email   =   StringField(label='Email', validators=[DataRequired(), Email()])
    text    =   StringField(label='Your message', validators=[DataRequired()])
    submit  =   SubmitField(label='send')