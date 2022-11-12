
from Sensor.Sensor_Data_Recoder.database.db import Database
from sqlalchemy import Table, Column, String, MetaData

class DBModels():
    def __init__(self):
        self.db = Database()
        self.meta = MetaData()

    def create_sensor_data_table(self, COL1, COL2):
        '''
        Method to create the sensor data table in DB
        Parameter: Columns
        '''
        SensorData = Table(
        'SensorData', self.meta,
        Column(f'{COL1}', String),
        Column(f'{COL2}', String),
        )
        self.meta.create_all(self.db.engine)

    def insert_data(self, timestamp, sensor_data):
        '''
        Method to insert data into the table
        '''
        __table__ = Table('SensorData', self.meta, autoload=True, autoload_with=self.db.engine)
        statement = __table__.insert().values(TIMESTAMP=f"{timestamp}", SENSOR_DATA=f"{sensor_data}")
        self.db.engine.execute(statement) 
