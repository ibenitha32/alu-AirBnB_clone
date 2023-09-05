# AirBnB Clone Console Readme
The objective of this project is to deploy a simplified version of the AirBnB website on a server. While it will not encompass all the features of the original platform, it will encompass enough fundamental concepts to serve as a foundation for higher-level programming.

## Initial Step: Develop a Command Interpreter for Managing AirBnB Objects
This initial step holds significant importance as it lays the groundwork for subsequent projects, including HTML/CSS templating, database storage, API integration, and front-end development.

## What is a Command Interpreter?
Think of it as similar to the Shell, but tailored to a specific use-case. In our context, we aim to manage the objects within our project with the following capabilities:

* Create a new object (e.g., a new User or a new Place)
* Retrieve an object from a file, a database, etc.
* Perform operations on objects (e.g., counting, computing statistics, etc.)
* Update attributes of an object
* Delete an object

## Running the Console
You can utilize the console in both interactive and non-interactive modes:

Interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

Non-interactive mode (similar to the C Shell project):
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Supported Commands:
* create - Create an object
* show - Display an object based on its ID
* destroy - Delete an object
* all - Show all objects, either of one specific type or all types
* update - Modify an instance based on the class name and ID
* quit/EOF - Exit the console
* help - Obtain descriptions of available commands

To initiate the console, use the following command in your shell:

```bash
AirBnB_clone$ ./console.py
(hbnb) 
```

## Create
To create an object, use the following format: "create <ClassName>" (e.g., `create BaseModel`).

```bash
(hbnb) create BaseModel
```

## Show
To display an instance based on its class name and ID, use the following format:

```bash
(hbnb) show BaseModel 1234-1234-1234
```

## Destroy
To delete an instance of an object, use the format: "destroy <ClassName> <id>" (e.g., `destroy BaseModel 1234-1234-1234`).

```bash
(hbnb) destroy BaseModel 1234-1234-1234
```

## All
To list all objects of a specific class or all classes, use one of the following formats:

```bash
(hbnb) all
(hbnb) all State
```

## Update
To update an instance based on its class name and ID, use the following format:

```bash
(hbnb) update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
```

## Quit
To exit the console, type "quit" or use the EOF (End of File) command.

## Help
To get information about a specific command or see a list of available commands, use the "help" command followed by the command name (e.g., `help quit`).

```bash
(hbnb) help quit
Defines quit option
(hbnb)
```

## Supported Classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

## Authors
* Benitha Iradukunda - <b.iradukund1@alustudent.com>
* Aime Magnifique Ndayishimiye - <a.ndayishim@alustudent.com>
