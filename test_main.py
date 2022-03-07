#!/usr/bin/python3
"""
    Basic Testing
    Before unittest
"""

from models.base_model import BaseModel
from models.base_model import storage

if __name__ == '__main__':

    """
        Execute some fast testing
    """

    num_test = 3

    if num_test == 1:
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
                                           type(my_model_json[key]),
                                           my_model_json[key]))

        print("--")
        my_new_model = BaseModel(**my_model_json)
        print(my_new_model.id)
        print(my_new_model)
        print(type(my_new_model.created_at))

        print("--")
        print(my_model is my_new_model)

        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)

    elif num_test == 2:
        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        print(my_model)

    elif num_test == 3:
        my_obj = storage.all()
        for key, val in my_obj.items():
            print("key {} ||| val: {} ".format(key, val))
    else:
        pass