#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Rafael Figueroa
Main Drone Code
"""

import sys
from time import sleep
import imu_fusion
from imu_fusion import imu_output

from socket_drone import Socket_drone
sck = Socket_drone()

while True:

    try:
        imu_data = imu_output()
        # print imu_data
        sck.send_data(imu_data)
        sleep(0.1)

    except KeyboardInterrupt:
        print 'closing socket'
        sck.close_socket()
        sys.exit()

