import sqlalchemy
import mysql.connector

host = "localhost"
user = "root"
password = "123"

db_string = "mysql+pymysql://"+user+":"+password+"@"+host+":3306/sensordata"

class Database:
    '''
    connect to the database
    '''
    def __init__(self):
        self.engine = sqlalchemy.create_engine(db_string, pool_size=200, max_overflow=10)

    def connect_db(self):
        '''
        Create DB instance
        '''
        try:
            self.create_db()
        except:
            pass
        try:
            self.create_table()
        except:
            pass
        self.connection = self.engine.connect()

    def create_db(self):
        '''
        Create a database
        '''
        mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE sensordata")

    def create_table(self):
        '''
        Create a table
        '''
        mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database="sensordata"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE sensordata (TIMESTAMP VARCHAR(255), SENSOR_DATA VARCHAR(255))")
