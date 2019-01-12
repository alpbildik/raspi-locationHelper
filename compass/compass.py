import py_qmc5883l
from math import sin, cos, asin

sensor = py_qmc5883l.QMC5883L()

def calibrate(calibration_matrix):
    sensor.set_calibration(calibration_matrix)

def read_compass_raw():
    return sensor.get_bearing_raw()


def read_compass():
    return sensor.get_bearing()



def read_compass_with_tilt():
    [x,y,z] = sensor.get_magnet_raw()
    
