from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

COFFEE_RATINGS = [
    ("☕"),
    ("☕☕"),
    ("☕☕☕"),
    ("☕☕☕☕"),
    ("☕☕☕☕☕")
]

WIFI_RATINGS = [
    ("🙅🏻‍♀️"),
    ("💪"),
    ("💪💪"),
    ("💪💪💪"),
    ("💪💪💪💪"),
    ("💪💪💪💪💪")
]

POWER_RATINGS = [
    ("🙅🏻‍♀️"),
    ("🔌"),
    ("🔌🔌"),
    ("🔌🔌🔌"),
    ("🔌🔌🔌🔌"),
    ("🔌🔌🔌🔌🔌")
]

class CafeForm(FlaskForm):

    cafe = StringField('Cafe name', validators=[DataRequired()])

    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL(message="Please enter a valid url maps location.")])

    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])

    close_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])

    rating = SelectField('Coffee Rating', choices=COFFEE_RATINGS, validators=[DataRequired()])

    wifi = SelectField('Wifi Strength Rating', choices=WIFI_RATINGS, validators=[DataRequired()])

    power = SelectField('Power Source Availability', choices=POWER_RATINGS, validators=[DataRequired()])

    submit = SubmitField('Submit')