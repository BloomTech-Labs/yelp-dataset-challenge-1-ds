# file to house business and review classes
from flask_test import db


class Business(db.Model):
    """Create class 'Business' for Yelp App
    Business has methods:
    --- id
    --- name
    --- location
    --- reviews (database relationship)
    
    added __repr__ function to show content of Business class as text (vs. as location in memory)"""
    
    id = db.Column(db.String(), primary_key = True)
    name = db.Column(db.String(), nullable=False)
    location = db.Column(db.String(), nullable=False)
    reviews = db.relationship('Review', backref='business', lazy=True)
    
    def __repr__(self):
        return '<NAME {}>'.format(self.name)


# create review class for sqlite database
class YelpReview(db.Model):
    """Create class 'Review' for Yelp App
    YelpReview has methods:
    - id
    - text
    - rating
    - business_id (if review is pulled through yelp API)
    
    added __repr__ function to show content of Review class as text (vs. as location in memory)"""
    
    id = db.Column(db.String(), primary_key = True)
    text = db.Column(db.Text(), nullable = False)
    rating = db.Column(db.Integer(), nullable = False)
    business_id = db.Column(db.String(), db.ForeignKey('business.id'))
    
    def __repr__(self):
        return '<TEXT {}>'.format(self.text)
    
class UserReview(db.Model):
    """Create class 'UserReview' for Yelp App
    UserReview has methods:
    - id
    - text
    - rating
    - business_id (if review is pulled through yelp API)
    
    added __repr__ function to show content of Review class as text (vs. as location in memory)"""
    
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Integer, nullable = False)
    
    def __repr__(self):
        return f"Review('{self.text}', '{self.rating}')"