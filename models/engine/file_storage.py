#!/usr/bin/python3
# Authors: mikiasHailu and yared Tsgie

""" This module is for the filestorage class """

import json
import datetime
import os

class FileStorage:

    """ THis is the file storage class """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """ This funciton will Sets new obj in objects dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """ This function will return all the functions """

        return FileStorage.__objects

    def save(self):
        """ This is the save function """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """ This function sill form a json flie """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                    for k, v in obj_dict.items()}

            FileStorage.__objects = obj_dict

    def classes(self):
        """ This class contain all the modules """
        from models.base_model import BaseModel
        from models.state import State
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                "State": State,
                "User": User,
                "Place": Place,
                "City": City,
                "Amenity": Amenity,
                "Review": Review}
        return classes

    def attributes(self):
        """ This function will return an attribute of the modules """
        attributes = {
                "BaseModel":
                {"id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime},
                "State":
                {"name": str},
                "User":
                {"email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str},
                "Place":
                {"city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list},
                "City":
                {"state_id": str,
                    "name": str},
                "Amenity":
                {"name": str},
                "Review":
                {"place_id": str,
                    "user_id": str,
                    "text": str}
                }
        return attributes
