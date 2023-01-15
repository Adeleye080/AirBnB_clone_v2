#!/usr/bin/python3
""" SQLAlchemy Database storage class """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place


class DBStorage:
    """
    Defines databse storage
    """
    __engine = None
    __session = None
    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, database), pool_pre_ping=True)

        if user == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query all objects
        """
        obj_list = [User, State, City, Amenity, Place, Review]
        tmp = {}
        if cls == None:
            for obj in obj_list:
                instance = self.__session.query(obj)
        else:
            if type(cls) is str:
                cls = eval(cls)
            instance = self.__session.query(cls)
            for obj in instance:
                tmp.update({obj.__class__.__name__ + '.' + obj.id: obj})
        return tmp;

    def new(self, obj):
        """
        adds object to database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commits all changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from database
        """
        if obj is not None:
            self.__session.delete(obj)
        else:
            return

    def reload(self):
        """
        create all tables and database session
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """calls remove()"""
        self.__session.close()
