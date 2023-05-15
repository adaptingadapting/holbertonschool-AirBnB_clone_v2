#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        def cities(self):
            """Return the list of City instances with state_id equal to
            the current State.id"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
