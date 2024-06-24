#!/bin/usr/bin

""" first state modle """
from SQLAlchemy import Column, Integer, String, MetaData
from SQLAlchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):


    """state class"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
