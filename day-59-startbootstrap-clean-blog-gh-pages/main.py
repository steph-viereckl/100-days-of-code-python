from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/7221495a65bd4f398ffb").json()

post_dict = {}

for post in posts:
    post_dict[post["id"]] = post

print(f"post_dict: {post_dict}")

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html", blog_posts=posts)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/post/<int:post_id>')
def blog_post(post_id):
    print(f"Post id: {post_id}")

    return render_template("post.html", blog_post=post_dict[post_id])

if __name__ == "__main__":
    app.run(port=5000, debug=True)


