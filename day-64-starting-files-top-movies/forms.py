from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, URL

class EditMovieForm(FlaskForm):

    rating = FloatField('Your Rating (i.e. 7.4)', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddMovieForm(FlaskForm):

    title = FloatField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')