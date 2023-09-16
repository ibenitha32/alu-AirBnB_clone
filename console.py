#!/usr/bin/python3
"""
This module defines the console for our project
"""
import cmd
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Defines the console
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF to exit the program
        """
        return True

    def emptyline(self):
        """
        Empty line
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in models.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = shlex.split(arg)
        objects = models.storage.all().values()
        if not arg:
            print([str(value) for value in objects])
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            print(
                [
                    str(value)
                    for key, value in models.storage.all().items()
                    if key.split(".")[0] == args[0]
                ]
            )

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute and save it to the JSON file.
        """
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                obj = models.storage.all()[key]
                if hasattr(obj, args[2]):
                    value = args[3]
                    if value[0] == '"' and value[-1] == '"':
                        value = value[1:-1]
                    setattr(obj, args[2], type(getattr(obj, args[2]))(value))
                    models.storage.save()
                else:
                    print("** attribute doesn't exist **")


if __name__ == "__main__":
    """
    Main function
    """
    HBNBCommand().cmdloop()

