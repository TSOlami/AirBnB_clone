#!usr/bin/python3
"""The Console Module"""
import cmd
import sys

class HBNBCommand(cmd.Cmd)

# chooses the console prompt
prompt = '(hbnb) ' 



if __name__ == '__main__':
    HBNBCommand().cmdloop()
