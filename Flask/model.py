"""
SQLAlchemy models for Yelp Text Analyzer Project
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import \
    (Column, Integer, String, ForeignKey, DateTime, Float, Binary, Text)
from sqlalchemy.orm import relationship

Base = declarative_base()

class Business(Base):
    """Create class 'Business' for Yelp App
    Business has methods:
    - id
    - name
    - location
    - reviews
    
    added __repr__ function to show content of Business class as text (vs. as location in memory)"""
    
    __tablename__ = 'businesses'
    
    id = Column(String, primary_key = True)
    name = Column(String(100))
    location = Column(String(100))
    reviews = relationship("Review", backref = 'business')
    
    def __repr__(self):
        return '<BUSINESS {}>'.format(self.name)


class Review(Base):
    """Create class 'Review' for Yelp Review Predictor App
    Review has methods:
    - id
    - text
    - stars
    - business_id
    
    added __repr__ function to show content of Review class as text (vs. as location in memory)"""
    
    __tablename__ = 'reviews'

    id = Column(String, primary_key=True)
    stars = Column(Float)
    text = Column(String(150))
    business_id = Column(String, ForeignKey('business.id'))

    def __repr__(self):
        return '<REVIEW {}>'.format(self.text)
    

