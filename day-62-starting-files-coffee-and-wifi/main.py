from fileinput import filename

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from forms import CafeForm
import csv
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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():

    form = CafeForm()
    if form.validate_on_submit():
        # Exercise:
        # Make the form write a new row into cafe-data.csv
        # with   if form.validate_on_submit()

        new_cafe = [form.data[key] for key in form.data if key not in ["submit", "csrf_token"]]
        print(f"form data: {form.data}")
        print(f"new_cafe: {new_cafe}")

        # mode "a" is append (w will overwrite)
        with open("cafe-data.csv", mode="a") as file:
            writer = csv.writer(file)
            writer.writerow(new_cafe)

        return render_template('cafes.html')

    else:
        return render_template('add.html', form=form)




@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        all_rows = []

        for row in csv_data:
            all_rows.append(row)

    print
    return render_template('cafes.html', cafes=all_rows)


if __name__ == '__main__':
    app.run(debug=True)
