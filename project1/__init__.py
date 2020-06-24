import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def create_app():
    app = Flask(__name__)

    # Check for environment variable
    # if not os.getenv("DATABASE_URL"):
    #     raise RuntimeError("DATABASE_URL is not set")

    # Configure session to use filesystem
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    URI="postgres://gmwsnpjuknwnsc:0bec7b99b1c9dc9a1afa9306a4d61f272fb1c2c4938e7f2824a7e686199f50c0@ec2-54-217-213-79.eu-west-1.compute.amazonaws.com:5432/dc4c5o7600qkku"

    # Set up database
    engine = create_engine(URI)
    db = scoped_session(sessionmaker(bind=engine))
    db.__init__(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/signin",methods = ["POST"])
    def signin():
        email = request.form.get("Email")
        passw =  request.form.get("Pass")

        chkpassw = db.execute("SELECT password FROM users WHERE email = :email",{"email":email}).fetchone()

        
        if(chkpassw==None):
            return render_template("error.html", message= "EMAIL NOT IN DATABASE PLEASE REGISTER.")
        elif(chkpassw!=passw):
            return render_template("error.html", message = "INCORRECT PASSWORD ")
        
        return render_template("")

    @app.route("/register")
    def register():
        return render_template("register.html")

    @app.route('/signup',methods= ["POST"])
    def signup():
        Name = request.form.get("Name")
        email = request.form.get("email")
        passw = request.form.get("pass")
        cpassw = request.form.get("cpass")
        prof = request.form.get("profession")
        chkbox = request.form.get("invalidCheck2")

        if(passw!=cpassw):
            return render_template("error.html",message="The passwords dont match :{ !!")

        # db.execute("CREATE TABLE users( id SERIAL PRIMARY KEY, Name VARCHAR NOT NULL, email VARCHAR NOT NULL, password VARCHAR NOT NULL, profession VARCHAR NOT NULL)");
        db.execute("INSERT INTO users(email, Name, password, profession) VALUES (:email, :Name, :password, :profession)",
        {"Name":Name, "email":email, "password":passw, "profession":prof})
        db.commit()

        return render_template("success.html", message="Registration sucessfull. Please redirect to Login Page to continue :}!")