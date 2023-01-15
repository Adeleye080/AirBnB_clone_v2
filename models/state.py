#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City',cascade="all, delete, save-update,\
                          delete-orphan", backref='state')

    @property
    def cities(self):
        from models import storage
        data = storage.all()
        results = []
        city_instance = []
        for key, value in data.items():
            if value.__class__.__name__ == "City":
                city_instance.append(data[key])
        for city in city_instance:
            if city.state_id == self.id:
                results.append(city)
        return results
