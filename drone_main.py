#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Rafael Figueroa
Main Drone Code
"""

from time import sleep
import imu_fusion
from imu_fusion import imu_output

from socket_drone import Socket_drone
sck = Socket_drone()

for t in range(0, 100):
    imu_data = imu_output()
    print imu_data
    sck.send_data(imu_data)
    sleep(0.1)

sck.close_socket()




