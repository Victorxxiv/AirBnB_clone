#!/usr/bin/python3
""" A module to handle file serialization and deserialization """

import json
import os.path
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review
from models.city import City


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
        FileSto_obj_dict["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """ Changes a __objects dict to a JSON file """
        FSobjdict = FileStorage.__objects
        obj_dict = {obj: FSobjdict[obj].to_dict() for obj in FSobjdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

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
