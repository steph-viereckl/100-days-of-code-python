from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.simple import EmailField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[
        DataRequired(),
        Email(message="Loser! Type in a real email"),
        Length(min=4, message="Uh type in more letters plz")
    ])
    password = PasswordField(label='Password', validators=[
        DataRequired(),
        Length(min=8, message="Please create a password with at least 8 characters.")
    ])
    submit = SubmitField(label="Login")