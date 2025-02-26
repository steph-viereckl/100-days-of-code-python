from calendar import error
from pprint import pprint
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Alternatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def get_random_cafe():

    result = db.session.execute(db.select(Cafe))
    random_cafe = choice(result.scalars().all())
    print(f"random cafe: {random_cafe.name}")

    cafe_json = jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })

    pprint(f"cafe json: {cafe_json}")

    return cafe_json

    # Alternatively, you can convert into dictionary and then use jsonify
    # Simply convert the random_cafe data record to a dictionary of key-value pairs.
    # return jsonify(cafe=random_cafe.to_dict())

@app.route("/all", methods=["GET"])
def get_all_cafes():

    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()

    all_cafes_dict = {"cafes": []}

    for cafe in all_cafes:
        all_cafes_dict["cafes"].append(cafe.to_dict())

    pprint(f"All Cafes: {all_cafes_dict}")

    return jsonify(all_cafes_dict)
    # Using list comprehension
    # return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search", methods=["GET"])
def cafe_search():
    search_location = request.args.get('loc')
    print(f"search: {search_location}")
    results = db.session.query(Cafe).filter(Cafe.location == search_location).all()
    #  Angelas way using where
    #  result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    # Note, this may get more than one cafe per location
    # all_cafes = result.scalars().all()

    pprint(f"results: {results}")

    if results:

        cafe_dict = {"cafes": []}

        for cafe in results:
            cafe_dict["cafes"].append(cafe.to_dict())

        return jsonify(cafe_dict)

    else:
        error_dict = {"error": {"Not Found": "Sorry, we don't have a cafe at that location"}}
        return jsonify(error_dict)

@app.route("/add", methods=["POST"])
def add_cafe():

    print(f"request name: {request.form['name']}")
    # When using postman you can mock up Body > urlencoded and it can be read just like
    # input tags!

    new_cafe = Cafe(
        name = request.form["name"],
        map_url = request.form["map_url"],
        img_url =request.form["img_url"],
        location = request.form["location"],
        seats = request.form["seats"],
        has_toilet = int(request.form["has_toilet"]),
        has_wifi = int(request.form["has_wifi"]),
        has_sockets = int(request.form["has_sockets"]),
        can_take_calls = int(request.form["can_take_calls"]),
        coffee_price = request.form["coffee_price"],
    )

    # Angelas solution
    # new_cafe = Cafe(
    #     name=request.form.get("name"),
    #     map_url=request.form.get("map_url"),
    #     img_url=request.form.get("img_url"),
    #     location=request.form.get("loc"),
    #     has_sockets=bool(request.form.get("sockets")),
    #     has_toilet=bool(request.form.get("toilet")),
    #     has_wifi=bool(request.form.get("wifi")),
    #     can_take_calls=bool(request.form.get("calls")),
    #     seats=request.form.get("seats"),
    #     coffee_price=request.form.get("coffee_price"),
    # )

    db.session.add(new_cafe)
    db.session.commit()

    # search_location = request.args.get('loc')
    return jsonify({"response": {"success": "Successfully added new cafe"}})


# http://127.0.0.1:5001/update-price/77?price=£5.75
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):


    # If you use the get or 404 method then an exception will be thrown
    # cafe_to_update = db.get_or_404(Cafe, cafe_id)
    cafe_to_update = db.session.get(Cafe, cafe_id)

    if cafe_to_update:
        cafe_to_update.coffee_price = request.args.get("price")
        db.session.commit()

        return jsonify({"response": {"success": "Successfully updated price"}})
    else:
        return jsonify({"error": {"Not Found": "Sorry, a cafe with that id cannot be found"}})

@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):

    if request.args.get("api-key") != "TopSecretApiKey":

        return jsonify({"error": {"Authentication Error": "Sorry, you do not have permission"}})

    else:

        cafe_to_delete = db.session.get(Cafe, cafe_id)

        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify({"response": {"success": "Successfully deleted cafe"}})
        else:
            return jsonify({"error": {"Not Found": "Sorry, a cafe with that id cannot be found"}})

# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True, port=5001)