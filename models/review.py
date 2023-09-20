#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """
    Review classto store review information

    Attributes:
        __tablename__ (str): Table associated with model
        text (str): Text content of the review
        place_id (str): Id of place being reviewed
        user_id (str): Id of user who worte the review
    """
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
