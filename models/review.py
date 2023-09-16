#!/usr/bin/python3
"""Defines the Review class, which inherits from BaseModel"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Review class for storing reviews"""

    place_id = ""
    user_id = ""
    text = ""
