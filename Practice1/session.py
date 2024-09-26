#Sessions
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key= "hello"
app.permanent_session_lifetime=timedelta(minutes=5)

@app.route('/')
def home():
    # return render_template("index.html", fname=name, lname="gupta" )
    return render_template("index.html")


@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        session.permanent=True
        user=request.form["nm"]
        session["user"]=user
        flash("login successful")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("already logged in")
            return redirect(url_for("user"))
        return render_template("login.html")
@app.route("/user")
# def user():
#     if "user" in session:
#         user=session["user"]
#         return f"<h1> hi {user}</h1>"
#     else:
#         return redirect(url_for("login"))

# when we want a different page for the user
def user():
    if "user" in session:
        user=session["user"]
        return render_template("user.html", user=user)
    else:
        flash("you rae not logged in")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user=session["user"]
        flash(f"You are logged out", "info")
    session.pop("user",None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)

# wwe can flash messages when we login or logout, for that we need to import flash