#!/usr/bin/python3

""" Initialize the FileStorage and reload data """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

