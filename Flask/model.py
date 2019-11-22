from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import \
    (Column, Integer, String, ForeignKey, DateTime, Float, Binary, Text)
from sqlalchemy.orm import relationship




class Review(Base):
    __tablename__ = 'reviews'

    review_id = Column(String, primary_key=True)
    date = Column(DateTime)
    cool = Column(Integer)
    funny = Column(Integer)
    useful = Column(Integer)
    stars = Column(Float)
    text = Column(Text)
    token_vector = Column(Text)
    token = Column(Text)
    ngram = Column(Text)
    noun_chunk = Column(Text)
    lemma = Column(Text)
    business_id = Column(String, ForeignKey('businesses.business_id'))
    user_id = Column(String, ForeignKey('users.user_id'))
