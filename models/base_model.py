#!/usr/bin/python3
"""Definition for base model class"""
import uuid
from datetime import datetime

class BaseModel:
    """ Base class for airbnb models"""
    def __init__(self, *args, **kwargs):
        """Instantiation of base model class"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')

            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """String representation of instance"""
        cls_name = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls_name, self.id, self.__dict__)
    
    def save(self):
        """Updates updated_time with current time when changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """convert instance to dict"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__': (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
    