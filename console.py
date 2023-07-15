#!/usr/bin/python3
"""
The `cmd` module is primarily used for creating custom interactive shells that allow users to interact with a program. In the Airbhb project, `console.py` serves as the command line interpreter's entry point.
"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """
    Command entry point of the command interpreter

    Returns:
        True or False
    """
    prompt = "(hbnb) "
    class_for_airbnb = {"BaseModel": BaseModel,
                      "User": User,
                      "State": State,
                      "City": City,
                      "Amenity": Amenity,
                      "Place": Place,
                      "Review": Review}

    def do_quit(self, args):
        """
        Exit the program
        """
        return True

    def do_EOF(self, args):
        """
        EOF command to end the program
        """
        print()
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in
        response to the prompt.
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of BAseModel, saves it
        (to the JSON file) and prints the id.

        Args:
            arg(str): given class in the command line interpreter
        if the class name is missing, print ** class name missing **
        if the class name doesnt exist, print ** class doesn't exist **
        """
        if not args:
            print("** class name missing **")

        elif args not in self.class_for_airbnb:
            print("** class doesn't exist **")

        else:
            instance = globals()[args]
            new = instance()
            new.save()
            print(new.id)

    def do_show(self, args):
        """
        String representation of an id instance
        """
        args = args.split()
        all_attributes = storage.all()
        if args is None or args == "":
            print("** class name missing **")

        elif args[0] not in self.class_for_airbnb:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args[0], args[1]) not in all_attributes:
            print("** no instance found **")

        else:
            print(all_attributes["{}.{}".format(args[0], args[1])])

    def do_destroy(self, args):
        """
        Command to destroy an instance
        """
        arg = args.split()
        all_attributes = storage.all()
        if not arg:
            print("** class name missing **")

        elif arg[0] not in self.class_for_airbnb.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in all_attributes:
            print("** no instance found **")

        else:
            del all_attributes["{}.{}".format(args.split()[0], args.split()[1])]
            storage.save()

    def do_all(self, args):
        """
        [all] prints all string representation
        all airbnb_instances based or not on the class name
        """
        args = args.split()
        instance_list = []
        if args and args[0] not in self.class_for_airbnb.keys():
            print("** class doesn't exist **")

        elif not args:
            for value in storage.all().values():
                instance_list.append(str(value))

        else:
            for value in storage.all().values():
                if args[0] == value.__class__.__name__:
                    instance_list.append(str(value))
        if len(instance_list):
            print(instance_list)

    def do_update(self, args):
        """
        [Update] is command to update attributes
        """
        all_attributes = storage.all()
        if len(args.split()) == 0:
            print("** class name missing **")

        elif args not in self.class_for_airbnb.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in all_attributes:
            print("** no instance found **")

        elif len(args.split()) == 2:
            print("** attribute name missing **")

        elif len(args.split()) == 3:
            print("** value missing **")

        else:
            key = "{}.{}".format(args.split()[0], args.split()[1])
            obj_update = args.split()[2]
            value = args.split()[3]
            setattr(storage.all()[key], obj_update, value)
            storage.save()

    def default(self, line):
        """
        [default method]

        Args:
        line ([str]): user's input
        Returns:
        [method]: returns the method needed or error
        """
        instance_list = (line.replace("(", ".").replace(",", ".").replace(" ", "")
                 [:-1].split("."))
        if len(instance_list) > 1:
            if instance_list[1] == "all":
                return self.do_all(instance_list[0])

            elif instance_list[1] == "show":
                return self.do_show(instance_list[0] + " " + instance_list[2])

            elif instance_list[1] == "destroy":
                return self.do_destroy(instance_list[0] + " " + instance_list[2])

            elif instance_list[1] == "update":
                return self.do_update(instance_list[0] + " " + instance_list[2] + instance_list[3] +
                                      " " + instance_list[4])

            elif instance_list[1] == "count":
                return self.do_count(instance_list[0])

        else:
            print("*** Unknown syntax: {}".format(line))
            return False

    def do_count(self, args):
        """
        Obtain the number of instance of a class: <class name>.count
        """
        instance_counter = 0
        airbnb_instances = storage.all()
        for key, value in airbnb_instances.items():
            if args in value.__str__():
                instance_counter += 1
        print(instance_counter)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
