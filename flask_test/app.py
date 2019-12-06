from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm, ReviewForm

app = Flask(__name__)
# secret key from flask app tutorial
app.config['SECRET_KEY'] = '789531f82597c4e6f638a3c40ac94a6c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Business(db.Model):
    """Create class 'Business' for Yelp App
    Business has methods:
    - id
    - name
    - location
    - review1
    - review1_id
    - review2
    - review2_id
    - review3
    - review3_id
    
    added __repr__ function to show content of Business class as text (vs. as location in memory)"""
    
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String())
    location = db.Column(db.String())
    review1 = db.Column(db.String())
    review1_id = db.Column(db.String())
    review2 = db.Column(db.String())
    review2_id = db.Column(db.String())
    review3 = db.Column(db.String())
    review3_id = db.Column(db.String())
    
    def __repr__(self):
        return '<NAME {}>'.format(self.name)


# create review class for sqlite database
class Review(db.Model):
    """Create class 'Review' for Yelp App
    Business has methods:
    - id
    - text
    
    added __repr__ function to show content of Review class as text (vs. as location in memory)"""
    
    id = db.Column(db.String, primary_key = True)
    text = db.Column(db.String())
    
    


# dummy review data for flask app display testing
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
    return render_template('about.html', title='About')

# define route for registration
# 'methods=['GET','POST']' allows users to submit forms on the page
# if there are no errors with registration, display successful account creation message, redirect to homepage
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

# define route for login
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.', 'danger')
    return render_template('login.html', title='Login', form=form)

# define route for manual review entry
@app.route("/review", methods=['GET', 'POST'])
def review():
    form = ReviewForm()
    return render_template('review.html', title='Write Your Own Review!', form=form)

# define route for businesses page
@app.route("/businesses")
def businesses():
    return render_template('businesses.html', title='Businesses')

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