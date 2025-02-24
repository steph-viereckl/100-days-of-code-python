from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from forms import EditMovieForm, MovieSearchForm
from movie_api import MovieFinder
import json
import ast


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

# Setup path to database on the Flask App
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

@app.route("/")
def home():

    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Movie).order_by(Movie.title))
    # Use .scalars() to get the elements rather than entire rows from the database
    movies = result.scalars().all()
    return render_template("index.html", movie_list=movies)


@app.route("/edit", methods=["GET", "POST"])
def update_movie():

    update_form = EditMovieForm()

    # It is a post method when user clicks "submit" on the edit page
    if update_form.validate_on_submit():
        print(f"Validate on submit")
        # GET MOVIE FROM WTF FORM
        new_rating = update_form.rating.data
        new_review = update_form.review.data

        # UPDATE MOVIE IN DATABASE
        movie_id = request.args.get('id')
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.rating = new_rating
        movie_to_update.review = new_review
        db.session.commit()

        return redirect(url_for('home'))

    # It is a get method when the user initially clicks the "update" button and needs to be redirected to update page
    else:
        return render_template("edit.html", form=update_form)


@app.route("/delete")
def delete_movie():

    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))

@app.route("/search", methods=["GET", "POST"])
def search_movies():

    search_form = MovieSearchForm()

    # Once user enters in movie title and clicks Submit
    if search_form.validate_on_submit():
        print(f"Validate on submit")
        # GET MOVIE FROM WTF FORM
        movie_title = search_form.title.data
        # CALL MOVIE API TO FIND MATCHING MOVIES
        movie_finder = MovieFinder(title_to_search=movie_title)
        return render_template("select.html", movie_results=movie_finder.search_results)

    # It is a get method when the user initially clicks the "update" button and needs to be redirected to update page
    else:
        return render_template("add.html", form=search_form)


@app.route("/add", methods=["GET", "POST"])
def add_movie():

    movie = request.args.get('selected_movie')
    movie_dict = ast.literal_eval(movie)

    new_movie = Movie(
        title=movie_dict["title"],
        year=movie_dict["release_date"][:4],
        description=movie_dict["overview"],
        rating=round(movie_dict["vote_average"],1),
        ranking=10,
        review="Test review here",
        img_url=f"https://image.tmdb.org/t/p/original{movie_dict["poster_path"]}"
    )

    db.session.add(new_movie)
    db.session.commit()
    print(f"new movie id: {new_movie.id}")
    return redirect(url_for('update_movie', id=new_movie.id))







if __name__ == '__main__':
    app.run(debug=True, port=5001)
