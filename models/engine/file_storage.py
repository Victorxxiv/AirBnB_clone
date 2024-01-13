#!/usr/bin/python3
""" A module to handle file serialization and deserialization """


import json
import os.path
from models.base_model import BaseModel


class FileStorage():
    """ Definition of the class Filestorage to handle storage of files """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns all the instances stored in a dictionary "__objects" """

        return FileStorage.__objects

    def new(self, obj):
        """ Adds a new Key-value pair into the dictionary __objects with
        key as <class name>.id and value as object created
        <class name> is the class  from which an object has been instantiated

        Args:
            obj: is the instance of the class to add to the dict __object
        """
        FileSto_obj_dict = FileStorage.__objects
        obj_class_name = obj.__class__.__name__
        key = "{}.{}".format(obj_class_name,obj.id)
        FileSto_obj_dict[key] = obj


    def save(self):
        """ Changes a __objects dict to a JSON file """

        FileSto_obj_dict = FileStorage.__objects
        new_dict = {}
        for k, v in FileSto_obj_dict.items():
            new_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, "+a") as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        """
        Deserializes the json file back __objects dict is
        Reloading objects from jsonfile
        """

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_d = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_d)(**obj))
            return