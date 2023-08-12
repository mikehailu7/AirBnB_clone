#!/usr/bin/python3
# Authors: mikiasHailu and yared Tsgie

""" This is the review class module """

from models.base_model import BaseModel

class Review(BaseModel):
    """ This class is the review class """
    place_id = ""
    user_id = ""
    text = ""
