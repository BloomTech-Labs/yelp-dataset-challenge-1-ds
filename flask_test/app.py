from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

reviews = [
    
    {
        'business': 'Pizza Palace',
        'review_id': '1234',
        'content': 'Good, not great.',
        'date_posted': 'April 20, 2018'
    },
    {
        'business': 'Coffee House',
        'review_id': '5412',
        'content': 'The Best!',
        'date_posted': 'June 20, 2018'
    }
    
]

# define route for home page
# posts = posts give access to data within template
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', reviews=reviews)

# define route for about page
@app.route("/about")
def about():
    return render_template('about.html')

# define route for businesses page
@app.route("/businesses")
def businesses():
    return render_template('businesses.html')

# allow app to run using "python app.py" in terminal
if __name__ == '__main__':
    app.run(debug=True)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB = SQLAlchemy(app)

# class Business(DB.Model):
#     """Create class 'Business' for Yelp App
#     Business has methods:
#     - id
#     - name
#     - location
    
#     added __repr__ function to show content of Business class as text (vs. as location in memory)"""
    
#     id = DB.Column(DB.String, 
#                    primary_key = True)
#     name = DB.Column(DB.String(100), 
#                      nullable = False)
#     business_location = DB.Column(DB.String(100))