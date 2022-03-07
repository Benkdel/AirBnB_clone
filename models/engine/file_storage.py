#!/usr/bin/python3
"""
    Persistency
"""

import json
from os import path


class FileStorage:
    """
        Class to serialize inst to JSON file
        and the other way arround

        Variables:
            file path = file storage
            objects = dictinary <class name>.id (ex: BaseModel.123151231)

    """

    __file_path = "file.json"
    __objects = dict()

    " =============== Public Methods ===================== "

    def all(self):
        """
            Return all objects from file
        """
        return (self.__objects)

    def new(self, obj):
        """
            Sets in __objetcs the obj with
            key <obj class name>.id
        """
        _key = "{0}.{1}".format(obj.__class__.__name__, obj.id)
        self.__objects[_key] = obj

    def save(self):
        """
            Serializes __objects dict
            to the JSON file in path
        """
        objs_dict = self.__objects.copy()

        for key, obj in self.__objects.items():
            objs_dict[key] = obj.to_dict()
        with open(self.__file_path, mode="w") as file_json:
            file_json.write(json.dumps(objs_dict))

    def reload(self):
        """
            Deserializes JSON file to __objects dict
            if file exists. otherwise do nothing, no exception should
            be rise
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        try:
            with open(self.__file_path, mode="r") as file_json:
                for key, values in json.load(file_json).items():
                    class_name = values["__class__"]
                    self.new(class_dict[class_name](**values))
        except Exception:
            pass
