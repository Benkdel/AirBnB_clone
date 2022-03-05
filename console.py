#!/usr/bin/python3
"""
    Adhoc console for
    AirBnB clone project
"""

import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        Wrapper class for cmd
    """
    intro = 'Welcome to the AirBnB-clone console'
    prompt = '(hbnb) '
    file = None

    " ===================== Console Methods / Helpers ================ "
    def parse(arg):
        print(arg.split())
        return (arg.split())

    " ===================== Model Methods ============================ "
    def do_print(self, arg):
        _list = []
        _list = arg.split()
        for item in _list:
            print(item)

    def do_create_obj(self, arg):
        B1 = BaseModel()
        print(B1)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
