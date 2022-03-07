#!/usr/bin/python3
"""
    Persistency
"""

import json
from lib2to3.pytree import Base
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
    __objects = {}

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
        filename = self.__file_path
        obj_dict = dict()

        if self.__objects is None or not self.__objects:
            pass
        else:
            for key, obj in self.__objects.items():
                obj_dict[key] = obj.to_dict()

                with open(filename, mode="a") as json_file:
                    json_file.write(json.dumps(
                        obj_dict, indent=2, sort_keys=True))

    def reload(self):
        """
            Deserializes JSON file to __objects dict
            if file exists. otherwise do nothing, no exception should
            be rise
        """
        from models.base_model import BaseModel

        print("Inside reload method from file storage ... ")

        filename = self.__file_path

        # try:
        if path.exists(filename) is True:
            with open(filename, mode="r") as json_file:
                cls_dict = json.load(json_file)
                for key, val in cls_dict.items():
                    # class_name = val["__class__"]
                    self.new(BaseModel(**val))

        # except BaseException:
        #    print("file not created")
        #    pass
