from sensor.exception import SensorException
import sys
import os



from sensor.logger import logging
#......from line 7 to 21 we just cheak our exception file working  or not by using 0 division erorr............
def test_exception():
    try:
        logging.info('division by zero error is comming')
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)
    

if __name__=="__main__":


    try:
        test_exception()

    except Exception as e:
        print(e)
