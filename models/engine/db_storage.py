#!/usr/bin/python3
"""Define the DBStorage class."""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate DBStorage."""
        # Set up your database engine
        # Set up your session

    def close(self):
        """Call remove() on the private session attribute
        or close() on the class Session."""
        self.__session.close()
