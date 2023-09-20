#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """
    A place to stay

    Attributes:
        __tablename__ (str): Table associated with model
        city_id (str): Id of city to which place belongs
        user_id (str): Id of user who owns place
        name (str): Name of the place
        description (str): Description of place
        number_rooms (str): Number of rooms in place
        number_bathrooms (str): Number of bathrooms in place
        max_guest (int): Maximum guests allowed
        price_by_night (int): Price per night for place
        latitude (float): Latitude coordinate of place
        longitude (float): Longitude coordinate of place
        amenity_ids (list): List of amenity ids associated with place
        reviews (relationship): rship representing reviews of place
    """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship('Review', backref='place', cascade='delete')

    if getenv("HBNB_TYPE_STORAGE", None) != 'db':
        @property
        def reviews(self):
            """Get list of linked reviews"""
            related_reviews = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    related_reviews.append(review)
            return related_reviews
