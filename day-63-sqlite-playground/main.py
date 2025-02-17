import sqlite3

# Open (or create if it doesn't exist
db = sqlite3.connect("books-collection.db")

# Cursor that will control out database.
cursor = db.cursor()

############ Create a table ############
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# CREATE TABLE - command that we are executing
# books - name of the table we are creating
# () - Fields in the table (columns in an excel file)
# id INTEGER PRIMARY KEY - First field. Named "id" and it be type of integer and is the PRIMARY KEY to make it unique
# title varchar(250) NOT NULL UNIQUE - "title" field that is 250 character string, cannot be empty (NOT NULL) and must be UNIQUE
# author varchar(250) NOT NULL = "author" field that cannot be empty and is a 250 character string
# rating FLOAT NOT NULL - "rating" field that is a FLOAT data type that cannot be empty

############ Add to a table ############
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

# As you've seen, writing SQL commands are complicated and error-prone. It would be much better if we could just write Python code and get the compiler to help us spot typos and errors in our code. That's why SQLAlchemy was created.
#
# SQLAlchemy is defined as an ORM (Object Relational Mapping) library.
# This means that it's able to map the relationships in the database into Objects.
# Fields become Object properties.
# Tables can be defined as separate Classes and each row of data is a new Object.
# This will make more sense after we write some code and see how we can create a Database/Table/Row of data using SQLAlchemy.