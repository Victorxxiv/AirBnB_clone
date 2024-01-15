#!/usr/bin/python3
"""Type module of BaseModel"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Defines all common attributes / methods for other classes """

    def __init__(self, *args, **kwargs):
        """
        Initializes the public instance variables or public data attributes
        Args:
            *args (list): named arguments
            **kwargs (dict): key-word arguments
                            "id" : the id for every instance created
                            "created_at" : the time an instance is created
                            "updated_at" : the sat which an instance is updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)
            self.updated_at = datetime.now()


    def save(self):
        """
        updates the self.update_at attribute with
        the current datetime
        """

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary for the attributes of an instance and
        adding more attributes of (a)time of creation,
        (b)time of update, (c)attribute for name of class
        """

        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """
        When we call print function on the model,
        this is the format of display
        """

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
