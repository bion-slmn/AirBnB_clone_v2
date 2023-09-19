#!/usr/bin/python3
'''this module creates a database engine'''
from os import getenv
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place
from models.amenity import Amenity


class DBStorage():
    '''this is the engine fordatabase'''
    __engine = None
    __session = None

    def __init__(self):
        ''' initalize values in to the class'''
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if (getenv('HBNB_ENV') == 'test'):  # drop all tables
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        '''query for a class if given or query for all classes'''

        if cls:
            if type(cls) == str:
                cls = eval(cls)
            result = self.__session.query(cls).all()
            newdict = {}
            for obj in result:
                key = f'{cls.__name__}.{obj.id}'
                value = obj
                newdict[key] = value
            return newdict
        objs = self.__session.query(State).all()
        objs.extend(self.__session.query(City).all())
        objs.extend(self.__session.query(User).all())
        objs.extend(self.__session.query(Place).all())
        objs.extend(self.__session.query(Review).all())
        objs.extend(self.__session.query(Amenity).all())
        return {f'{type(o).__name__}.{o.id}': o for o in objs}

    def new(self, obj):
        '''add the object to the current database session'''
        self.__session.add(obj)

    def save(self):
        ''' commit all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete from the current database session obj if not None'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''create all tables in the database'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
