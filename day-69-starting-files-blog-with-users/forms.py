from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Email, Length
from wtforms.fields.simple import EmailField, PasswordField
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = EmailField(label="Email", validators=[DataRequired(), Email(message="Please enter a valid email")])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, message="Please create a password with at least 8 characters.")])
    submit = SubmitField(label="Register")

class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), Email(message="Please enter a valid email")])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")

class CommentForm(FlaskForm):
    body = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField(label="Submit Comment")
