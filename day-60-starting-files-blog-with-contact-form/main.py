from flask import Flask, render_template, request
import requests
from notification_manager import NotificationManager

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():

    print(f'method: {request.method}')

    if request.method == "POST":
        # print(f'name: {}')
        # print(f'email: {request.form["email"]}')
        # print(f'phone: {request.form["phone"]}')
        # print(f'message: {request.form["message"]}')
        submitted = True

        email = NotificationManager()
        email.send_email(
            name=request.form["name"],
            email=request.form["email"],
            phone=request.form["phone"],
            message=request.form["message"]
        )

    else:
        submitted = False

    print(f"submitted: {submitted}")
    return render_template("contact.html", response_submitted=submitted)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)




if __name__ == "__main__":
    app.run(debug=True, port=5001)
