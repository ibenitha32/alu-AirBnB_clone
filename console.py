#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
    }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Pass when an empty line is entered"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        args = split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(args[0])()
            new_object.save()
            print(new_object.id)

    def do_show(self, line):
        """Prints the string representation of an instance."""
        args = split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance."""
        args = split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representations of instances."""
        args = split(line)
        objects = []
        if not args:
            objects = storage.all().values()
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            objects = [obj for obj in storage.all().values() if type(obj).__name__ == args[0]]
        print([str(obj) for obj in objects])

    def do_update(self, line):
        """Updates an instance by adding or updating an attribute."""
        args = split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                instance = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3]
                try:
                    attr_value = eval(attr_value)
                except (NameError, SyntaxError):
                    pass
                setattr(instance, attr_name, attr_value)
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

