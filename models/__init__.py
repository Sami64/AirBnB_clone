#!/usr/bin/python3
""" Instantiates the storage engine """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()