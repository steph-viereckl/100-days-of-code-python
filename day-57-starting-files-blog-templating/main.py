from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)
post_dict = {}

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=blog_url)
posts_json = response.json()

for post in posts_json:
    # Get post id (i.e. "2")
    post_id = int(post["id"])
    # Add to dictionary of Posts so it can be easily grabbed when clicked
    post_dict[post_id] = Post(post)

@app.route('/')
def home():
    # Pass the list of posts to show on main page
    return render_template("index.html", posts=post_dict.values())

@app.route('/post/<int:id>')
def show_post(id):
    # Find the specific post by id and render post
    return render_template("post.html", post=post_dict.get(id))

if __name__ == "__main__":
    app.run(debug=True)
