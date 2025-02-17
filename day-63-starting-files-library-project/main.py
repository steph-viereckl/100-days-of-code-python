from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# Create the Flask App
app = Flask(__name__)

# Create the SQLAlchemy Database
class Base(DeclarativeBase):
  pass

# Create the Extension
database = SQLAlchemy(model_class=Base)

# Configure the SQL database for the app in the instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"

# initialize the app with the extension
database.init_app(app)



# The use of ":" means we are explicitly declaring a variable type. In this, we are explicity saying that
# id is the type of "Mapped"
class Book(database.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# Create table schema in the database. Requires application context.
with app.app_context():
    database.create_all()

all_books = []

@app.route('/')
def home():


    results = database.session.execute(database.select(Book).order_by(Book.title))
    all_books = results.scalars().all()

    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        new_book = Book(
            title=request.form["name"],
            author=request.form["author"],
            rating=request.form["rating"]
        )

        print(f"Adding new book: {new_book}")
        database.session.add(new_book)
        database.session.commit()

        return redirect(url_for('home'))
    else:
        return render_template("add.html")

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_rating(id):

    print(f"book_id: {id}")
    if request.method == "POST":
        print(f"In post method: {id}")
        new_rating = request.form["new_rating"]
        print(f"New rating: {new_rating}")

        book_to_update = database.session.execute(database.select(Book).where(Book.id == id)).scalar()
        book_to_update.rating = new_rating
        database.session.commit()

        return redirect(url_for('home'))
    else:
        print(f"Get book")
        # to get single element we can use scalar()
        book_result = database.session.execute(database.select(Book).where(Book.id == id)).scalar()
        print(f"returned_book: {book_result}")
        print(f"returned_book.title: {book_result.title}")
        return render_template("edit_rating.html", book=book_result)

# Angela's solution doesn't pass the id in the parameter to the method and she uses the arg function to get it instead
# @app.route("/edit", methods=["GET", "POST"])
# def edit():
#     if request.method == "POST":
#         # UPDATE RECORD
#         book_id = request.form["id"]
#         book_to_update = db.get_or_404(Book, book_id)
#         book_to_update.rating = request.form["rating"]
#         db.session.commit()
#         return redirect(url_for('home'))
#     book_id = request.args.get('id')
#     book_selected = db.get_or_404(Book, book_id)
#     return render_template("edit_rating.html", book=book_selected)



@app.route("/delete/<id>", methods=["GET"])
def delete_book(id):

        book_to_delete = database.session.execute(database.select(Book).where(Book.id == id)).scalar()
        database.session.delete(book_to_delete)
        database.session.commit()
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, port=5001)

