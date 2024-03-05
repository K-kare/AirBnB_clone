#!/usr/bin/python3
#command interpreter in python
import cmd

class Myconsole(cmd.Cmd):
    prompt = '(hbnb)'
    def do_EOF(self, args):
        """shows end of a file"""
        print()
        return True
    def do_quit(self, args):
        """This exits the program"""
        return True
if __name__ == '__main__':
    Myconsole().cmdloop()
