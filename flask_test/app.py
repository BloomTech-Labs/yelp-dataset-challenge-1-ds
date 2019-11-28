from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(app)

class Business(DB.Model):
    """Create class 'Business' for Yelp App
    Business has methods:
    - id
    - name
    - location
    
    added __repr__ function to show content of Business class as text (vs. as location in memory)"""
    
    id = DB.Column(DB.String, 
                   primary_key = True)
    name = DB.Column(DB.String(100), 
                     nullable = False)
    business_location = DB.Column(DB.String(100))