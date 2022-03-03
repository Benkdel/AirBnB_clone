#!/usr/bin/python3
"""
    Super Class
"""

import json
import os.path
import uuid
from datetime import datetime

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
                    val = datetime.now().strftime(time_format)
                if key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().strftime(time_format)
            self.updated_at = datetime.now().strftime(time_format)

    " ===================== Public instance methods ================== "

    def save(self):
        """
            Saves instance and
            updates datetime
        """
        self.updated_at = datetime.now().strftime(time_format)

    def to_dict(self):
        """
            Return dict rep of
            the instance
        """
        inst_dict = dict()
        for key, val in self.__dict__.items():
            if key in ["created at", "updated at"]:
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
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    
