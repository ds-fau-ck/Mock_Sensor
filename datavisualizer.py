from Sensor.Sensor_Data_Visualization.controller.controller import SensorDataFetchController
from Sensor.Sensor_Data_Visualization.database.db import Database
from Sensor.Sensor_Data_Visualization.models.model import DBModels

def data_visualizer():
    #connect to the database
    connect_to_db = Database()
    connect_to_db.connect_db()
    print("[ INFO ] DATABASE CONNECTED")

    # send a request to controller for storing data
    data_store = SensorDataFetchController()
    data_store.plot_sensor_data()

if __name__ == "__main__":
    
     data_visualizer()