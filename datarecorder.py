from Sensor.Sensor_Data_Recoder.controller.controll import SensorDataController
from Sensor.Sensor_Data_Recoder.database.db import Database
from Sensor.Sensor_Data_Recoder.models.model import DBModels

def data_recoder():
    #connect to the database
    connect_to_db = Database()
    connect_to_db.connect_db()
    print("[ INFO ] DATABASE CONNECTED")

    # send a request to controller for storing data
    data_store = SensorDataController()
    data_store.sensor_data()


if __name__ == "__main__":
     data_recoder()
     