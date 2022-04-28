import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


    

class Onecharacter(Base):
    __tablename__ = 'onecharacter'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False, unique=True)
    character_props = Column(String(250), nullable=False)

class Allcharacters(Base):
    __tablename__ = 'allcharacters' 
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('onecharacter.id'))
    character = relationship(Onecharacter)

class Onevehicle(Base):
    __tablename__ = 'onevehicle'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250), nullable=False, unique=True)
    vehicle_props = Column(String(250), nullable=False)
    
class Oneplanet(Base):
    __tablename__ = 'oneplanet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False, unique=True)
    planet_props = Column(String(250), nullable=False)

class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('onecharacter.id'))
    onecharacter = relationship(Onecharacter)
    vehicle_id = Column(Integer, ForeignKey('onevehicle.id'))
    onevehicle = relationship(Onevehicle)
    planet_id = Column(Integer, ForeignKey('oneplanet.id'))
    oneplanet = relationship(Oneplanet)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    favourites_id = Column(Integer, ForeignKey('favourites.id'))
    favourites = relationship(Favourites)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')