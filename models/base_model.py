#!/usr/bin/python3
"""
    Super Class
"""

import json
import os.path
import uuid
from datetime import datetime
from models import storage


time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
        Base class
    """

    def __init__(self, *args, **kwargs):
        """
            Constructor: BaseModel object

            *Args:
                - Non dict argument list
            **kwargs
                - Dict argument list
        """
        if len(kwargs) > 0:
            for key, val in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    val = datetime.strftime(val, time_format)
                if key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    " ===================== Public instance methods ================== "

    def save(self):
        """
            Saves instance and
            updates datetime
        """
        self.updated_at = datetime.now()
        storage.new(self)

    def to_dict(self):
        """
            Return dict rep of
            the instance
        """
        inst_dict = dict()
        for key, val in self.__dict__.items():
            if key in ["created at", "updated at"]:
                inst_dict[key] = val.isoformat()
            elif val:
                inst_dict[key] = val

        inst_dict["__class__"] = self.__class__.__name__
        return (inst_dict)

    " ==================== Builtins ================================== "

    def __str__(self):
        """
            String Rep of BaseModel Class
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)


if __name__ == '__main__':
    """
        Execute some fast testing
    """

    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key,
              type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
