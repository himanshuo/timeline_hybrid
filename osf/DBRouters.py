__author__ = 'this awesome dude here.'
from osf.models import *


class DBRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if type(model) is Timeline:
            return 'pg'
        elif type(model) is History:
            return 'mongo'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if type(model) is Timeline:
            return 'pg'
        elif type(model) is History:
            return 'mongo'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if type(obj1) is Timeline and type(obj2) is Timeline:
            return True
        if type(obj1) is History and type(obj2) is History:
            return True
        if type(obj1) is Timeline and type(obj2) is History:
            return False
        if type(obj1) is History and type(obj2) is Timeline:
            return False
        return None


    def allow_migrate(self, db, model):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """

        if db == 'mongo' or type(model) is History:
            return False
        elif db == 'pg':
            return type(model) is Timeline
        return None