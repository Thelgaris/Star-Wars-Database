import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    onecharacter = relationship(Onecharacter)  



class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('oneplanet.id'))
    oneplanet = relationship(Oneplanet) 

class OnePlanet(Base):
    __tablename__= 'oneplanet'
    id = Column(Integer, primary_key=True)
    oneplanet_props = Column(string(250), Integer, string(250))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    vehicles_id = Column(Integer, ForeignKey('onevehicle.id'))
    onevehicle = relationship(Onevehicle)

class Onevehicle(Base):
    __tablename__= 'onevehicle'
    id = Column(Integer, primary_key=True)
    onevehicle_props = Column(string(250), Integer, string(250))

class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'), unique=True)
    characters = relationship(Characters)
    planets_id = Column(Integer, ForeignKey('planets.id'), unique=True)
    planets = relationship(Planets)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'), unique=True)
    vehicles = relationship(Vehicles)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')