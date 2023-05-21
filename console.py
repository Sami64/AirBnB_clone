#!/usr/bin/python3
""" Console Module """
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand Class"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''