#!/usr/bin/python3
"""This module defines a class to manage file storage for airbnb clone"""
import json

class FileStorage:
    """ Class manages storage of all instances for airbnb clone """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dictionary of all objects """
        return FileStorage.__objects
    
    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """ Saves dict to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """ Loads dict from file"""
        from models.base_model import BaseModel
        classes = {
            'BaseModel': BaseModel
        }

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass