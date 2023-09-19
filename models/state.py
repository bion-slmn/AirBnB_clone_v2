#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from models.city  import City
from sqlalchemy.orm import relationship
import models
from os.environ import get


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relat:wqionship('City', backref='state', cascade='all, delete')
    
    if get("HBNB_TYPE_STORAGE") != "db":
        @property
         def cities(self):
            '''getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id'''
            
            city_objs = model.storage.all(City)
            return [c_obj for c_obj in city_objs.values() 
                    if c_obj.state_id == self.id]
