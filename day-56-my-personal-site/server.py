from flask import Flask, render_template
# from flask import render_template

app = Flask(__name__)

# This decorator function will check to see what webpage the user is at. If they are on the homepage (i.e. www.google.com/) then it will run this
@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
