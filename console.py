#!/usr/bin/python3
#command interpreter in python
import cmd
from models import storage
import json

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    def do_EOF(self, args):
        """shows end of a file"""
        print()
        return True
    def do_quit(self, args):
        """This exits the program"""
        return True
    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass
    def do_create(self, line):
        """Creates an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.i)
    def do_show(self, line):
        """Prints the string representation of an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
