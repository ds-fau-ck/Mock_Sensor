import numpy
import time
import keyboard
from Sensor.Sensor_Data_Recoder.models.model import DBModels
#from models.model import DBModels
import matplotlib.pyplot as plt
import statistics
import warnings

warnings.filterwarnings('ignore')

class SensorDataController:
    '''
    controller class used to handle the data storing requests
    '''
    def __init__(self):
        self.insert_into_db = DBModels()
    
    def sensor_data(self):
        '''
        generate sensor data and store it into the database
        '''
        try:
            self.insert_into_db.create_sensor_data_table("TIMESTAMP", "SENSOR_DATA")
        except: 
            pass
        sensor_data_list = []
        interval = int(input("Please select an interval [1/2/3]: "))
        print("ENTER DISTRIBUTION: \n1) Normal Distribution. 2) Binomial Distribution.")
        random_distribution = int(input("Please select a random distribution [1/2]:"))
        if random_distribution==1:
            distribution = numpy.random.normal(size=1)
        elif random_distribution==2:
            distribution = numpy.random.binomial(n=50, p=0.5, size=1)
        else:
            print("[ ERROR ] RANDOM DISTRIBUTION DOES NOT EXIST.")
        print("Press 'A' to get min value.\nPress 'B' to get max value.")
        print("Press 'C' to get average value.\nPress 'D' to get variance value.")
        print("Press 'E' to get deviation value.\nPress 'F' to get median value.")
        print("[INFO] --- YOU MIGHT NEED TO PRESS KEYS MORE THAN ONCE TO GET THE RESULTS ---")
        while True:
            current_timestamp = time.time()
            time.sleep(interval)
            self.insert_into_db.insert_data(current_timestamp, distribution[0])
            # CALCULATIONS FOR THE INCOMING DATA
            sensor_data_list.append(int(distribution[0]))
            min_value = min(sensor_data_list)
            max_value = max(sensor_data_list)
            avg_value = sum(sensor_data_list)/len(sensor_data_list)
            try:
                variance_value = statistics.variance(sensor_data_list)
            except:
                variance_value = 0
            std_value = statistics.pstdev(sensor_data_list)
            median_value = statistics.median(sensor_data_list)
            final_data = {
                "min": min_value,
                "max": max_value,
                "average": avg_value,
                "variance": variance_value,
                "deviation": std_value,
                "median": median_value
            }
            if keyboard.is_pressed('a'):
                print("min:", final_data["min"])
            if keyboard.is_pressed('b'):
                print("max:", final_data["max"])
            elif keyboard.is_pressed('c'):
                print("average:", final_data["average"])
            elif keyboard.is_pressed('d'):
                print("variance:", final_data["variance"])
            elif keyboard.is_pressed('e'):
                print("deviation:", final_data["deviation"])
            elif keyboard.is_pressed('f'):
                print("median:", final_data["median"])
