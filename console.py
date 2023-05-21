#!/usr/bin/python3
""" Console Module """
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand Class"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    def do_quit(self, command):
        """ Quit command to exit the program """
        exit()

    def help_quit(self):
        """ Help quit command """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        print()
        exit()

    def help_EOF(self):
        """ Help EOF command """
        print("EOF command to exit the program")

    def emptyline(self):
        """ Empty line """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()