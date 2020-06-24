import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

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
# db.__init__(app)


db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, Name VARCHAR NOT NULL, Email VARCHAR NOT NULL, Password VARCHAR NOT NULL, Profession VARCHAR NOT NULL)")
# db.execute("DROP TABLE flights")