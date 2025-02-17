from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import sqlite3

# Create the Database
class Base(DeclarativeBase):
  pass

# Create the extension
# Need to pass pass a subclass of DeclarativeBase to the constructor of the database.
db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# initialize the app with the extension
db.init_app(app)

# The use of ":" means we are explicitly declaring a variable type. In this, we are explicity saying that
# id is the type of "Mapped"
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

    # Adding item to database.
    # If you don't add in the id, it will be auto-generated.
    new_book = Book(
        id = 1,
        title = "Harry Potter",
        author = "J.K. Rowling",
        rating = 10
    )

    # db.session.add(new_book)
    # db.session.commit()

    # To read records...
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # Result will be the rows in the database as a Result object
    # Scalars will return individual elements rather than entire rows
    all_books = result.scalars()
    print(f"Reading the db result: {result}")
    print(f"Reading the db all books: {all_books}")

    # to get single element we can use scalar()
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

    # Update by searching and matching agaisnt the book title
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

    # Update by finding book with primary key
    book_id = 1
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

    #Delete book with primary key
    book_id = 1
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()