#!/usr/bin/python3
"""
   Create 1 fileStorage per app
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
