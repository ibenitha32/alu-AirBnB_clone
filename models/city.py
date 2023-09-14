#!/usr/bin/python3
""" Defines city class that inherits from BaseModel. """

from models.base_model import BaseModel

class City(BaseModel):
    """The city class with attributes state_id and name. """
    state_id = ""
    name = ""
