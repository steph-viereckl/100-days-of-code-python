from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.now().year

    # Can add as many keyword arguments (kwargs) as we want
    # Need to have a name
    return render_template("index.html", num=random_number, curr_year=current_year)

@app.route('/guess/<name>')
def predictor(name):
    param = {"name": name}

    gender_response = requests.get(url="https://api.genderize.io", params=param)
    gender = gender_response.json()["gender"]

    age_response = requests.get(url="https://api.agify.io", params=param)
    age = age_response.json()["age"]

    # Can add as many keyword arguments (kwargs) as we want
    # Need to have a name
    return render_template("index.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)


