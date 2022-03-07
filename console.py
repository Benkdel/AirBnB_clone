#!/usr/bin/python3
"""
    Adhoc console for
    AirBnB clone project
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        Wrapper class for cmd
    """
    intro = 'Welcome to the AirBnB-clone console'
    prompt = '(hbnb) '
    file = None

    def do_quit(self, args):
        """
            Quit command to exit the program\n
        """
        return True

    def do_EOF(self, args):
        """
            EOF command to exit the program\n
        """
        print("")
        return True

    def emptyline(self):
        """
            Does not perform any action
        """
        pass

    def help_help(self):
        """
            Prints help command description
        """
        print("Provides description of a given command")

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
