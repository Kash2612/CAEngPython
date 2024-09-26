from crypt import methods

from flask import Flask, render_template, url_for, redirect,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rides.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age_limit = db.Column(db.Integer, nullable=False)
    height_limit = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)


rides = [
    {"name": "Roller Coaster", "age_limit": 12, "height_limit": 140, "price": 10},
    {"name": "Ferris Wheel", "age_limit": 0, "height_limit": 0, "price": 5},
    {"name": "Bumper Cars", "age_limit": 8, "height_limit": 120, "price": 7},
    {"name": "Haunted House", "age_limit": 10, "height_limit": 0, "price": 8},
    {"name": "Merry-Go-Round", "age_limit": 0, "height_limit": 0, "price": 4},
    {"name": "Water Slide", "age_limit": 5, "height_limit": 100, "price": 6},
    {"name": "Log Flume", "age_limit": 6, "height_limit": 110, "price": 7},
    {"name": "Swing Ride", "age_limit": 0, "height_limit": 0, "price": 5},
    {"name": "Drop Tower", "age_limit": 12, "height_limit": 130, "price": 9},
    {"name": "Go-Karts", "age_limit": 10, "height_limit": 130, "price": 15},
]

def populate_database():
    # Check if the database is empty
    if Ride.query.count() == 0:
        for ride_data in rides:
            new_ride = Ride(
                name=ride_data['name'],
                age_limit=ride_data['age_limit'],
                height_limit=ride_data['height_limit'],
                price=ride_data['price']
            )
            db.session.add(new_ride)
        db.session.commit()

# Create the database tables
with app.app_context():
    db.create_all()
    populate_database()




@app.route('/',methods=["POST","GET"])
def login():
    if request.method=="POST":
        username=request.form["username"]
        email=request.form["email"]
        role=request.form["role"]

        if role=="admin":
            return redirect(url_for("admin_dashboard"))
        else:
            return redirect((url_for("user_dashboard")))

    return render_template("login.html")


@app.route('/admin')
def admin_dashboard():
    return render_template("admin.html")

@app.route('/admin/rides')
def admin_view():
    rides = Ride.query.all()  # Get all rides from the database
    return render_template("view.html", rides=rides)


@app.route('/addride')
def add_ride_page():
    return render_template("addride.html")


@app.route('/rides', methods=['POST'])
def add_ride():
    name = request.form['name']
    age_limit = int(request.form['age_limit'])
    height_limit = int(request.form['height_limit'])
    price = float(request.form['price'])

    # ride_id = len(rides) + 1  # Simple way to assign an ID
    # rides.append({"id": ride_id, "name": name, "age_limit": age_limit, "height_limit": height_limit, "price": price})

    new_ride = Ride(name=name, age_limit=age_limit, height_limit=height_limit, price=price)
    db.session.add(new_ride)
    db.session.commit()

    return redirect(url_for('admin_view'))

@app.route('/updateride')
def update_ride_page():
    return render_template("updateride.html")

@app.route('/rides/update', methods=['POST'])
def update_ride():
    ride_id = int(request.form['ride_id'])
    # for ride in rides:
    #     if ride['id'] == ride_id:
    #         if request.form['new_name']:
    #             ride['name'] = request.form['new_name']
    #         if request.form['new_age_limit']:
    #             ride['age_limit'] = int(request.form['new_age_limit'])
    #         if request.form['new_height_limit']:
    #             ride['height_limit'] = int(request.form['new_height_limit'])
    #         if request.form['new_price']:
    #             ride['price'] = float(request.form['new_price'])
    #         break
    ride = Ride.query.get(ride_id)

    if ride:
        if request.form['new_name']:
            ride.name = request.form['new_name']
        if request.form['new_age_limit']:
            ride.age_limit = int(request.form['new_age_limit'])
        if request.form['new_height_limit']:
            ride.height_limit = int(request.form['new_height_limit'])
        if request.form['new_price']:
            ride.price = float(request.form['new_price'])

        db.session.commit()
    return redirect(url_for('admin_view'))

@app.route('/deleteride')
def delete_ride_page():
    return render_template("deleteride.html")

@app.route('/rides/delete', methods=['POST'])
def delete_ride():
    ride_id = int(request.form['ride_id'])
    # global rides
    # rides = [ride for ride in rides if ride['id'] != ride_id]

    ride = Ride.query.get(ride_id)

    if ride:
        db.session.delete(ride)
        db.session.commit()
    return redirect(url_for('admin_view'))

@app.route('/user', methods=['GET', 'POST'])
def user_dashboard():
    if request.method == 'POST':
        age = int(request.form['age'])
        height = int(request.form['height'])

        # Filtering rides based on age and height
        available_rides = []
        total_price = 0

        for ride in rides:
            if age >= ride["age_limit"] and (ride["height_limit"] == 0 or height >= ride["height_limit"]):
                available_rides.append(ride)
                total_price += ride["price"]

        return render_template('result.html', available_rides=available_rides, total_price=total_price, age=age, height=height)

    return render_template('user.html',rides=rides)

@app.route('/logout')
def logout():
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)