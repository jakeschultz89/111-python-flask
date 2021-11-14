from flask import Flask #from the flask module import the Flask class

app = Flask(__name__) #we are instantiating our Flask class 
                        # into your app variable


@app.route("/") # a decorator that creates a new HTTP path
def index(): #in the context of flask, this is a view function
    return "<h1>Hello, world!</h1>" #return statement


@app.route("/users/jake")
def about_jake():
    me = {
        "first_name": "Jake",
        "last_name": "Schultz",
        "hobbies": "video games",
        "active": True
    }
    return me

# mystring = "Hello, %s %s!" % (first_name, last_name)

@app.route("/greeting/<name>")
def print_name(name):
    return "<h1>Hello, %s!</h1>" % name


@app.route("/square/<int:num>")
def square_num(num):
    return "<h1>That number squared is: %s</h1>" % (num ** 2 )