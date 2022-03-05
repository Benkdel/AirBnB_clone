#!/usr/bin/python3
"""
    Persistency
"""

import json


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
        filename = self.__file_path
        obj_dict = dict()

        if self.__objects is None or not self.__objects:
            pass
        else:
            for key, obj in self.__objects.items():
                obj_dict[key] = obj.to_dict()

                with open(filename, mode="a") as json_file:
                    json_file.write(json.dumps(obj_dict))    

    def reload(self):
        """
            Deserializes JSON file to __objects dict
            if file exists. otherwise do nothing, no exception should
            be rise  
        """
        pass
