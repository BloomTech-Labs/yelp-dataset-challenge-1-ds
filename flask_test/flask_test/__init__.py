"""initialize yelp flask app"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# secret key from flask app tutorial
app.config['SECRET_KEY'] = '789531f82597c4e6f638a3c40ac94a6c'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flask_test import routes