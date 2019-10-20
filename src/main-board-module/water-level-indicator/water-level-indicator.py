"""
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: water-level-indicator.py
 * Author : Sashwat K
 * Created on : 10 Oct 2019
 * Last updated : 18 Oct 2019
 * Microcontroller: Raspberry Pi Zero W
 * Purpose: The main controller
"""

import RPi_I2C_driver
import os
from time import *

tankModuleAdress = 0x05
valveModuleAddress = 0x04


def i2cRunCommand(address, value):
    bashCommand = 'i2cset -y 1 ' + str(address) + ' ' + str(value)
    os.system(bashCommand)
    pass


i2cRunCommand(valveModuleAddress, 1)
