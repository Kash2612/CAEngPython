from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is home page <h1> HELLO </h1>"

# @app.route('/about')
# def aboutus():
#     return "You are using flask"
#
# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("home")) #we have to pass the name of the function in url_for instead of the route

# redirect to specific functions that take arguments
# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name="Admin"))


#If the module is being run directly (like python script.py), __name__ is set to '__main__'.
# If the module is being imported into another module, __name__ is set to the module's name.
if __name__ == '__main__':
    app.run()
