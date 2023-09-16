#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
import shlex
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "EOF command to exit the program"
        return True

    def do_create(self, line):
        "Creates a new instance of BaseModel, saves it, and prints the id"
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        new_instance = storage.classes()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        "Prints the string representation of an instance by class name and id"
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        all_instances = storage.all()
        if key not in all_instances:
            print("** no instance found **")
        else:
            print(all_instances[key])

    def do_destroy(self, line):
        "Deletes an instance by class name and id"
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        all_instances = storage.all()
        if key not in all_instances:
            print("** no instance found **")
        else:
            del all_instances[key]
            storage.save()

    def do_all(self, line):
        "Prints all string representations of instances based on class name"
        args = shlex.split(line)
        all_instances = storage.all()
        if not args:
            print([str(instance) for instance in all_instances.values()])
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        print([str(instance) for instance in all_instances.values() if type(instance).__name__ == class_name])

    def do_update(self, line):
        "Updates an instance by class name and id with a new attribute value"
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        all_instances = storage.all()
        if key not in all_instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        instance = all_instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def emptyline(self):
        "Passes on empty line input"
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

