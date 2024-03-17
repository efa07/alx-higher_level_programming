#!/usr/bin/python3
"""
Python file that contains the class definition of State and an instance
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base as deb

Base = deb()


class State(Base):
    """
    State class that inherits from Base

    Attributes:
        id: Id state
        name: Name of state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
