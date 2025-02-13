from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import os
from dotenv import load_dotenv
from my_form import LoginForm

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
# Get Secret Key from env file
load_dotenv()
app.secret_key = os.environ.get("SECRET_KEY", "Secret Key cannot be found")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    print("Login Page")
    login_form = LoginForm()

    # If successfully submitted
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    # Otherwise just keep the user on the login success
    else:
        return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
