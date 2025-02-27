from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor
from flask_ckeditor import CKEditorField

class PostForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author Name', validators=[DataRequired()])
    img_url = StringField('Background Image URL', validators=[DataRequired()])
    body = CKEditorField('Body')
    submit = SubmitField('Submit')

