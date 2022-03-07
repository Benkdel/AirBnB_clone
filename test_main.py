#!/usr/bin/python3
"""
    Basic Testing
    Before unittest
"""

from models.base_model import BaseModel
from models.base_model import storage
from models.engine.file_storage import FileStorage
import os

if __name__ == '__main__':

    """
        Execute some fast testing
    """

    num_test = 12

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
        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)

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

    elif num_test == 8:
        fs = FileStorage()
        file_path = "file.json"
        try:
            file_path = FileStorage._FileStorage__file_path
        except:
            pass
        try:
            os.remove(file_path)
        except:
            pass
        try:
            fs._FileStorage__objects.clear()
        except:
            pass
        ids = []
        objs_by_id = {}
        for i in range(10):
            bm = BaseModel()
            fs.new(bm)
            bm.save()
            ids.append(bm.id)
            objs_by_id[bm.id] = bm

        try:
            fs._FileStorage__objects.clear()
        except:
            pass
        fs.reload()

        all_reloaded = fs.all()

        if len(all_reloaded.keys()) != len(ids):
            print("Missing after reload")

        for id in ids:
            if all_reloaded.get(id) is None and all_reloaded.get("{}.{}".format("BaseModel", id)) is None:
                print("Missing {}".format(id))

        for id in ids:
            obj_reloaded = all_reloaded.get(id)
            if obj_reloaded is None:
                obj_reloaded = all_reloaded.get(
                    "{}.{}".format("BaseModel", id))
            print(obj_reloaded.__class__.__name__)
            obj_created = objs_by_id[id]
            print(obj_reloaded.id == obj_created.id)
            print(obj_reloaded.created_at == obj_created.created_at)
            print(obj_reloaded.updated_at == obj_created.updated_at)

        try:
            os.remove(file_path)
        except Exception as e:
            pass

    elif num_test == 12:
        
        class FileStorage(FileStorage):
            def all(self):
                """ DOC
                """
                return {}

    else:
        pass
