#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from models.city  import City
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        '''getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id'''
        from models import storage
        city_objs = storage.all(City)
        return [c_obj for c_obj in city_objs.values() 
                if c_obj.state_id == self.id]
