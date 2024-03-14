#!/usr/bin/python3
"""
Defines the State class that links to the MySQL table states
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City
from sqlalchemy.ext.declarative import declarative_base


class State(Base):
    """
    Represents a State
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
