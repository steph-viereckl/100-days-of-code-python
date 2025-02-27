from pprint import pprint

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from forms import PostForm

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # Method that returns this object as a dictionary
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():

    # Get blog posts from the database
    result = db.session.execute(db.select(BlogPost))
    all_posts = result.scalars().all()

    posts = []

    # Create a list of python dictionaries
    for post in all_posts:
        posts.append(post.to_dict())

    return render_template("index.html", all_posts=posts)

@app.route('/post/<post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)

# Either of these works.. I'm not sure what the best approach is?
# @app.route('/post')
# def show_post():
#     post_id = request.args.get("post_id")
#     print(f"Post id: {post_id}")
#     requested_post = db.get_or_404(BlogPost, post_id)
#     return render_template("post.html", post=requested_post)

# TODO: add_new_post() to create a new blog post
@app.route("/new_post", methods=["GET", "POST"])
def add_new_post():

    form = PostForm()

    # On "POST"
    if form.validate_on_submit():

        # Take data from form and create new blog post
        new_post = BlogPost()
        new_post.title = form.title.data
        new_post.subtitle = form.subtitle.data
        new_post.author = form.author.data
        new_post.img_url = form.img_url.data
        new_post.body = form.body.data
        new_post.date = date.today().strftime("%B %d, %Y")

        # Add to Database
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('get_all_posts'))

    # On GET (first landing on empty form)
    else:
        return render_template("make-post.html", form=form, heading_text="Create New Post")


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):

    # Get selected post and default fields
    current_post = db.get_or_404(BlogPost, post_id)
    form = PostForm(
        title=current_post.title,
        subtitle=current_post.subtitle,
        author=current_post.author,
        img_url=current_post.img_url,
        body=current_post.body
    )

    # On "POST"
    if form.validate_on_submit():

        # Take data from form and create new blog post
        current_post.title = form.title.data
        current_post.subtitle = form.subtitle.data
        current_post.author = form.author.data
        current_post.img_url = form.img_url.data
        current_post.body = form.body.data

        # Update in Database
        db.session.commit()

        return redirect(url_for('show_post', post_id=post_id))

    # On GET (first landing on empty form)
    else:
        return render_template("make-post.html", form=form, heading_text="Edit Post")


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<post_id>", methods=["GET"])
def delete_post(post_id):

    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()

    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
