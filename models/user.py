#!/usr/bin/python3
""" Definition for user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class for airbnb clone"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
