import MySQLdb

DB_HOST = 'localhost'
DB_PORT = 3307
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_NAME = 'testdb'

class Singleton:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None
    def __call__(self, *args, **kwds):
        if(self.instance == None):
            self.instance = self.klass(*args, **kwds)
        return self.instance

@Singleton
class Database:
    connection = None
    def get_connection(self):
        if(self.connection is None):
            self.connection = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME, port=DB_PORT)
        return self.connection

db1 = Database().get_connection()
db2 = Database().get_connection()

print(db1)
print(db2)
