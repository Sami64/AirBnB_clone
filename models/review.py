#!/usr/bin/python3
""" Definition for review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for airbnb clone"""

    place_id = ""
    user_id = ""
    text = ""
