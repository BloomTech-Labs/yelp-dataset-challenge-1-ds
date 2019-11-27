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
    - reviews (from linked relationship to 'Review' class)
    
    added __repr__ function to show content of Business class as text (vs. as location in memory)"""
    
    id = DB.Column(DB.String, 
                   primary_key = True)
    name = DB.Column(DB.String(100), 
                     nullable = False)
    business_location = DB.Column(DB.String(100))
    
    # def __repr__(self):
    #     return '<BUSINESS {}>'.format(self.name)


# class Review(DB.Model):
#     """Create class 'Review' for Yelp Review Predictor App
#     Review has methods:
#     - id
#     - text
#     - rating
#     - business_id (foreign key linked from 'Business' class)
#     - business (relationship identified with 'Business' class, facilitates '.reviews' User method)
    
#     added __repr__ function to show content of Review class as text (vs. as location in memory)"""

#     id = DB.Column(DB.String, primary_key = True)
#     rating = DB.Column(DB.Float)
#     text = DB.Column(DB.String(150))
#     business_id = DB.Column(DB.String, 
#                             DB.ForeignKey('business.id'), 
#                             nullable = False)
#     business = DB.relationship('Business', 
#                                backref = DB.backref('reviews', lazy = True))

#     def __repr__(self):
#         return '<REVIEW {}>'.format(self.text)
    

