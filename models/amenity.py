#!/usr/bin/python3
"""Defining an amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent the amenity.
    Attributes:
        name (str): Name of the amenity.
    """

    name = ""
