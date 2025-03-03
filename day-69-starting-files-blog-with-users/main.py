from datetime import date
from pprint import pprint
from functools import wraps

from flask import Flask, abort, render_template, redirect, url_for, flash, request, g
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# Flask Login Manager
# The login manager contains the code that lets your application and Flask-Login work together,
# such as how to load a user from an ID, where to send users when they need to log in, and the like.
login_manager = LoginManager()
# # Once the actual application object has been created, you can configure it for login with:
login_manager.init_app(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB with the UserMixin
class User(UserMixin, db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    # This will act like a List of BlogPost objects attached to each User.
    # The "author" refers to the author property in the BlogPost class.
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"

    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    # Create reference to the User object. The "posts" refers to the posts property in the User class.
    author = relationship("User", back_populates="posts")

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # ***************Parent Relationship*************#
    comments = relationship("Comment", back_populates="parent_post")

class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")

    # ***************Child Relationship*************#
    post_id: Mapped[str] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    text: Mapped[str] = mapped_column(Text, nullable=False)

with app.app_context():
    db.create_all()

def is_logged_in():

    print(f'Current User: {current_user}')
    print(f'Current User is authenticated: {current_user.is_authenticated}')
    if current_user.is_authenticated:
        return True
    else:
        return False

def is_admin():
    if current_user.get_id() == "1":
        return True
    else:
        return False

def admin_only(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if current_user.get_id() == "1":
            return function(*args, **kwargs)
        else:
            return abort(403)

    return decorated_function

@app.route('/')
def get_all_posts():

    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()

    return render_template("index.html", all_posts=posts, logged_in=is_logged_in(), is_admin=is_admin())


@app.route('/register', methods=["GET", "POST"])
def register():

    print("Register method")
    register_form = RegisterForm()

    # If POST, it is when the user clicks "Submit" on the register page
    # Add credentials to database and redirect user to secrets page
    if request.method == "POST":

        email = register_form.email.data
        user_name = register_form.name.data

        # Find user by email entered.
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        # If user email already exists, redirect to login screen
        if user:
            flash('Username already exists. Please login.')
            return redirect(url_for('login', message="You have already registered this email."))

        # Otherwise, create user
        else:

            hashed_password = generate_password_hash(
                register_form.password.data,
                method='pbkdf2:sha256',
                salt_length=8
            )

            new_user = User(
                name = user_name,
                email = email,
                password = hashed_password
            )

            db.session.add(new_user)
            db.session.commit()

            # Log in and authenticate user after adding details to database.
            login_user(new_user)
            return redirect(url_for('get_all_posts'))

    # If GET, we are initially navigating to register page
    else:
        return render_template("register.html", form=register_form, logged_in=is_logged_in())


@app.route('/login', methods=['GET', 'POST'])
def login():

    print(f"Method: {request.method}")
    print(f"Current User: {current_user}")

    login_form = LoginForm()

    if request.method == "POST":

        # Get inputs from form
        email = login_form.email.data
        password = login_form.password.data

        # Find user by email entered.
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        # If user cannot be found, tell user and refresh page
        if not user:
            flash('Invalid Username')
            return redirect(url_for('login'))

        # Otherwise, check if password is correct
        elif check_password_hash(user.password, password):
            login_user(user)
            flash('You were successfully logged in')
            return redirect(url_for('get_all_posts'))

        else:
            flash('Invalid Password')
            return redirect(url_for('login', logged_in=is_logged_in()))

    # If GET method, show login form
    else:
        return render_template('login.html', form=login_form, logged_in=is_logged_in())


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts', logged_in=is_logged_in()))

# You will need to provide a user_loader callback. This callback is used to reload the
# user object from the user ID stored in the session. It should take the str ID of a user,
# and return the corresponding user object. For example:
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@app.route("/post/<int:post_id>")
@login_required
def show_post(post_id):

    comment_form = CommentForm()
    requested_post = db.get_or_404(BlogPost, post_id)

    return render_template("post.html", post=requested_post, logged_in=is_logged_in(), form=comment_form)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts", logged_in=is_logged_in()))
    return render_template("make-post.html", form=form, logged_in=is_logged_in())


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id, logged_in=is_logged_in()))
    return render_template("make-post.html", form=edit_form, is_edit=True, logged_in=is_logged_in())


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts', logged_in=is_logged_in()))


@app.route("/about")
def about():
    return render_template("about.html", logged_in=is_logged_in())


@app.route("/contact")
def contact():
    return render_template("contact.html", logged_in=is_logged_in())


if __name__ == "__main__":
    app.run(debug=True, port=5004)
