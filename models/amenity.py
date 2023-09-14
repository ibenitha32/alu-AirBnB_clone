#!/usr/bin/python3
""" Defines amenity class that inherits from BaseModel. """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ The amenity class representing a model with a 'name' attribute. """
    name = ""
