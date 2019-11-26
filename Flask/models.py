"""
SQLAlchemy models for Yelp Text Analyzer Project
"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Business(DB.Model):
    """Create class 'Business' for Yelp App
    Business has methods:
    - id
    - name
    - location
    - reviews
    
    added __repr__ function to show content of Business class as text (vs. as location in memory)"""
    
    __tablename__ = 'businesses'
    
    id = DB.Column(DB.String, 
                   primary_key = True)
    name = DB.Column(DB.String(100), 
                     nullable = False)
    location = DB.Column(DB.String(100))
    reviews = DB.relationship("Review", backref = DB.backref('business', lazy = True)
    
    def __repr__(self):
        return '<BUSINESS {}>'.format(self.name)


class Review(DB.Model):
    """Create class 'Review' for Yelp Review Predictor App
    Review has methods:
    - id
    - text
    - stars
    - business_id
    
    added __repr__ function to show content of Review class as text (vs. as location in memory)"""
    
    __tablename__ = 'reviews'

    id = DB.Column(DB.String, primary_key = True)
    stars = DB.Column(DB.Float)
    text = DB.Column(DB.String(150))
    business_id = DB.Column(DB.String, 
                            DB.ForeignKey('business.id'), 
                            nullable = False)

    def __repr__(self):
        return '<REVIEW {}>'.format(self.text)
    

