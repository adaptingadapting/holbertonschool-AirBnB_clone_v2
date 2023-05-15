#!/usr/bin/python3
"""comments"""

from models.user import User
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv

modelos = {"User": User, "State": State,
           "City": City, "Amenity": Amenity,
           "Place": Place, "Review": Review}


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(('mysql+mysqldb://{}:{}@{}/{}')
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        objects = {}
        # if cls is None:
        for c in modelos:
            if modelos[c] == cls or cls is None:
                for key in self.__session.query(modelos[c]).all():
                    key = "{}.{}".format(__name__+'.'+key.id)
        return objects

    def new(self, obj):
        """new"""
        self.__session.add(obj)

    def save(self):
        """save"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete"""
        if obj is None:
            self.__session.delete(obj)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        ssession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ssession)
        self.__session = Session

    def close(self):
        """close"""
        self.__session.close()
