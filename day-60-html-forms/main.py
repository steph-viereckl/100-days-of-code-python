from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login_page():
    print(f'name: {request.form["name"]}')
    print(f'password: {request.form["password"]}')

    return render_template("login.html", name=request.form["name"])

if __name__ == "__main__":
    app.run(port=5000, debug=True)


