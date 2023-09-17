#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Creating a new User --")
my_user = User()
my_user.first_name = "Corry"
my_user.last_name = "Holberton"
my_user.email = "airbnb@holbertonshool.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Creating a new User 2 --")
my_user2 = User()
my_user2.first_name = "James"
my_user2.email = "airbnb2@holbertonshool.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)
