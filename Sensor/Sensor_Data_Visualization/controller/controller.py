from Sensor.Sensor_Data_Visualization.models.model import DBModels
import matplotlib.pyplot as plt
import keyboard
import statistics
import warnings
import pandas, numpy

warnings.filterwarnings('ignore')

class SensorDataFetchController:
    '''
    controller class used to handle the data fetching requests
    '''
    def __init__(self):
        self.insert_into_db = DBModels()
        self.counter = 0
    
    def sensor_data_fetch(self):
        '''
        fetch sensor data from the database
        '''
        result = self.insert_into_db.fetch_data()
        timestamp = result[self.counter+1][0]
        sensor_data = result[self.counter+1][1]
        return timestamp, sensor_data

    def plot_sensor_data(self):
        '''
        Method to plot sensor data diagram
        '''
        sensor_data_list, timestamp_list = [], []
        choose_plot = int(input("1) LINE PLOT. 2) SCATTER PLOT. 3) HISTOGRAM PLOT\nPlease select a plot for sensor data [1/2/3]: "))
        choose_calculation_plot = int(input("1) BAR PLOT. 2) PIE PLOT.\nPlease select a plot for calculations [1/2]: "))
        print("\nDATABASE ACCESS OPTIONS:\nPress 'a' to fetch all records.\nPress 'f' to fetch first record.\nPress 'l' to fetch last record.")
        while True:
            if keyboard.is_pressed('q'):
                break
            elif keyboard.is_pressed('a'):
                result = self.insert_into_db.fetch_data()
                print("ALL RECORDS: ", result)
            elif keyboard.is_pressed('f'):
                result = self.insert_into_db.fetch_data()
                print("FIRST RECORD: ", result[0])
            elif keyboard.is_pressed('l'):
                result = self.insert_into_db.fetch_data()
                print("LAST RECORD: ", result[-1])
            # DRAW PLOT FOR THE INCOMING DATA
            plt.subplot(1, 2, 1)
            timestamp, sensor_data = self.sensor_data_fetch()
            sensor_data_list.append(int(sensor_data))
            timestamp_list.append(timestamp)
            if choose_plot == 1:
                plt.xlabel("TIMESTAMP")
                plt.ylabel("SENSOR VALUE")
                plt.title("SENSOR DATA PLOT")
                df = pandas.DataFrame(list(zip(timestamp_list, sensor_data_list)), columns =['TIMESTAMP', 'SENSOR_DATA'])
                df.plot.line(reuse_plot=True, legend=False)
            elif choose_plot == 2:
                plt.xlabel("TIMESTAMP")
                plt.ylabel("SENSOR VALUE")
                plt.title("SENSOR DATA PLOT")
                plt.scatter(timestamp, sensor_data)
            elif choose_plot == 3:
                plt.xlabel("SENSOR VALUE")
                plt.title("SENSOR DATA PLOT")
                plt.hist(sensor_data)
            plt.pause(1)
            # CALCULATIONS FOR THE INCOMING DATA
            plt.subplot(1, 2, 2)
            plt.xlabel("NAME")
            plt.ylabel("VALUE")
            plt.title("SENSOR DATA CALCULATIONS")
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
            if choose_calculation_plot == 1:
                plt.bar(final_data.keys(), final_data.values(), color ='b',width = 0.4)
                
            elif choose_calculation_plot == 2:
                calculation_list = [min_value, max_value, avg_value, variance_value, std_value, median_value]
                plt.pie(numpy.array(calculation_list), labels=final_data.keys())
            self.counter += 1