#!/usr/bin/python3
# Authors: mikiasHailu and yared Tsgie
""" THis User class module """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class representing a User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
