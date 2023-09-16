#!/usr/bin/python3
"""Defines a FileStorage class for serializing and deserializing instances to/from JSON"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    Class FileStorage
    Represents a storage engine for serializing instances to a JSON file
    and deserializing JSON data back to instances.
    """

    def __init__(self, file_path="file.json"):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """Return a dictionary of all stored objects"""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to JSON file"""
        serialized_data = {}
        for key, obj in self.__objects.items():
            serialized_data[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_data, file)

    def reload(self):
        """Deserializes JSON data from the file into objects"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name = obj_data['__class__']
                    obj = eval(class_name)(**obj_data)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

