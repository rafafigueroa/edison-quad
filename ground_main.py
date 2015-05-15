#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Rafael Figueroa
Ground Station 
"""

import sys
from time import sleep
from gui_ground import GUI_quad
from socket_ground import Socket_ground
import numpy as np
    
# Script
GUI = GUI_quad()
sck = Socket_ground()

for a in range(0, 100):
    
    try:
        X = np.array([0, 0, 0, np.pi/(a+4.0), 0, np.pi/2.0])
        GUI.set_state(X)
        GUI.update_gui()
        drone_data = sck.receive_data()
        #sleep(0.1)

    except KeyboardInterrupt:
        print 'closing socket'
        sck.close_socket()
        sys.exit()

