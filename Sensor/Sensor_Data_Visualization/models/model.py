from Sensor.Sensor_Data_Visualization.database.db import Database
#from database.db import Database
from sqlalchemy import Table, Column, String, MetaData

class DBModels():
    def __init__(self):
        self.db = Database()
        self.meta = MetaData()

    def fetch_data(self):
        '''
        Method to get data from the table
        '''
        table = Table(
            'SensorData',
            self.meta,
            autoload = True,
            autoload_with = self.db.engine
        )

        get_result = table.select()
        conn = self.db.engine.connect()
        results = conn.execute(get_result)
        for result in results:
            result = results.fetchall()
            return result
