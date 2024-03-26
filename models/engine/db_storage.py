#!/usr/bin/python3
"""
Module for the DBStorage class, which manages database interaction.
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class DBStorage:
    """
    Class to handle database interaction, including:

    * Establishing connection
    * Adding, saving, and deleting objects
    * Querying for objects
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes DBStorage:
        * Fetches database credentials from environment variables
        * Creates a database engine
        * Drops tables in 'test' environments
        """

    def all(self, cls=None):
        """
        Queries the database, fetching objects, optionally filtered by class.

        Args:
            cls (class, optional): Specifies the class to filter results.

        Returns:
            dict: A dictionary of objects, with keys like 'ClassName.id'.
        """

    def new(self, obj):
        """
        Adds an object to the current database session for future saving.

        Args:
            obj: The object to be added.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits pending changes from the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object (if provided) from the current database session.

        Args:
            obj: The object to be deleted.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Initializes database tables and creates a new database session.
        """

    def close(self):
        """
        Closes the current database session.
        """
        self.__session.remove()
