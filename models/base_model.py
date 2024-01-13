#!/usr/bin/python3
""" Definition of models module """

import models
import uuid
from datetime import datetime


class BaseModel():
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

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "created_at":
                    if isinstance(v, str):
                        self.created_at = datetime.strptime(v, time_format)
                    else:
                        self.created_at = v
                elif k == "updated_at":
                    if isinstance(v, str):
                        self.updated_at = datetime.strptime(v, time_format)
                    else:
                        self.updated_at = v
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """
        updates the self.update_at attribute with
        the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary for the attributes of an instance and
        adding more attributes of (a)time of creation,
        (b)time of update, (c)attribute for name of class
        """

        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_ati \
            .strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return (my_dict)
