import flask
import werkzeug
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# Flask Login Manager
# The login manager contains the code that lets your application and Flask-Login work together,
# such as how to load a user from an ID, where to send users when they need to log in, and the like.
login_manager = LoginManager()
# Once the actual application object has been created, you can configure it for login with:
login_manager.init_app(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB with the UserMixin
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    print("Register method")

    # If POST, it is when the user clicks "Submit" on the register page
    # Add credentials to database and redirect user to secrets page
    if request.method == "POST":

        hashed_password = werkzeug.security.generate_password_hash(
            request.form.get("password"),
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = User(
            name = request.form.get("name"),
            email = request.form.get("email"),
            password = hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to database.
        login_user(new_user)

        return redirect(url_for('secrets'))

    # If GET, we are initially navigating to register page
    else:
        return render_template("register.html", logged_in=current_user.is_authenticated)




@app.route('/login', methods=['GET', 'POST'])
def login():

    print(f"Method: {request.method}")
    print(f"Current User: {current_user}")

    if request.method == "POST":

        # Get inputs from form
        email = request.form.get("email")
        password = request.form.get("password")

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
            return redirect(url_for('secrets'))

        else:
            flash('Invalid Password')
            return redirect(url_for('login'))

    # If GET method, show login form
    else:
        return render_template('login.html', logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download', methods=["GET"])
@login_required
def download():
    return send_from_directory(
        directory='static',
        path="files/cheat_sheet.pdf",
        as_attachment=False
    )

# You will need to provide a user_loader callback. This callback is used to reload the
# user object from the user ID stored in the session. It should take the str ID of a user,
# and return the corresponding user object. For example:
@login_manager.user_loader
def load_user(user_id):
    print("Load user")
    return db.get_or_404(User, user_id)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
