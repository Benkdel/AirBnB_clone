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
    prompt = '(hbnb)'

    def do_quit(self, args):
        """
            Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
            EOF command to exit the program
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
