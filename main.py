from sensor.exception import SensorException
import sys
import os
from sensor.logger import logging
from sensor.utils import dumb_csv_file_to_mongodb_collection
#......from line 7 to 21 we just cheak our exception file working  or not by using 0 division erorr............
# def test_exception():
#     try:
#         logging.info('division by zero error is comming')
#         a=1/0
#     except Exception as e:
#         raise SensorException(e,sys)
    

if __name__=="__main__":
    file_path='/home/shreyas/Desktop/projects/sensor_fault_detection/aps_failure_training_set1.csv'
    database_name="shreyas"
    collection_name="sensor"
    dumb_csv_file_to_mongodb_collection(file_path,database_name,collection_name)


    # try:
    #     test_exception()

    # except Exception as e:
    #     print(e)