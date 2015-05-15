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

while True:
    
    try:
        drone_msg = sck.receive_data()
        if drone_msg is not None:
            msg_list = drone_msg.split(' ')
            hx = float(msg_list[0].split(':')[1])
            hy = float(msg_list[1].split(':')[1])
            hz = float(msg_list[2].split(':')[1])

            X = np.array([0, 0, 0, hx, hy, hz])
            GUI.set_state(X)
            GUI.update_gui()
            
        else:
            print 'no data received'

    except KeyboardInterrupt:
        print 'closing socket'
        sck.close_socket()
        sys.exit()

