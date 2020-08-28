from django.conf import settings

class DatabaseQCRouter(object):
    """
    A router to control all database operations on models for different
    databases.

    In case an app is not set in settings.DATABASE_APPS_MAPPING, the router
    will fallback to the `default` database.

    Settings example:

    DATABASE_APPS_MAPPING = {'model_name1': 'db1', 'model_name2': 'db2'}

    """
    @staticmethod
    def db_for_read(self, model, **hints):
        """Point all read operations to the specific database."""
        #return settings.DATABASE_APPS_MAPPING.get(model._meta.sparqls, None)
        print("model._meta",model._meta,model.__dict__)
        if model._meta in ['polls.query', 'polls.choice']:
            return settings.DATABASE_APPS_MAPPING.get('qc', None)
        return None   


    @staticmethod
    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        #return settings.DATABASE_APPS_MAPPING.get(model._meta.sparqls, None)
        print("model._meta",model._meta,model.__dict__)
        if model._meta in ['polls.query', 'polls.choice']:
            return settings.DATABASE_APPS_MAPPING.get('qc', None)
        return None     


    def allow_relation(self, obj1, obj2, **hints):
        """Have no opinion on whether the relation should be allowed."""
        return None
       
class DatabaseDefaultRouter(object):
    """
    A router to control all database operations on models for different
    databases.

    In case an app is not set in settings.DATABASE_APPS_MAPPING, the router
    will fallback to the `default` database.

    Settings example:

    DATABASE_APPS_MAPPING = {'model_name1': 'db1', 'model_name2': 'db2'}

    """
    @staticmethod
    def db_for_read(self, model, **hints):
        """Point all read operations to the specific database."""
        #print("model._meta",model._meta,model.__dict__)
        if model._meta not in  ['polls.query', 'polls.choice']:
            return settings.DATABASE_APPS_MAPPING.get('default', None)    
        return None


    @staticmethod
    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        if model._meta not in  ['polls.query', 'polls.choice']:
            return settings.DATABASE_APPS_MAPPING.get('default', None)    
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Have no opinion on whether the relation should be allowed."""
        return True      
    '''    
    """
    @staticmethod
    def allow_migrate(db, app_label, model_name=None, **hints): # if using Django version 1.8
        """Have no opinion on whether migration operation is allowed to run. """
        print("allow_migrate",db,app_label, model_name, hints)
        if model_name == 'sparqlquery':
            return db == 'sparqls'
        return db == 'default'  
    """
    """
    @staticmethod
    def allow_migrate(db, app_label, model_name=None, **hints): # if using Django version 1.8
        """Have no opinion on whether migration operation is allowed to run. """
        print("allow_migrate",db,app_label, model_name, hints)
        if model_name == 'sparqlquery':
            return db == 'sparqls'
        return db == 'default'
    """
    """
    def allow_migrate(db, app_label, **hints): # if using Django version 1.8
        """Have no opinion on whether migration operation is allowed to run. """
        print("allow_migrate",db,app_label, hints)
        return True
'''