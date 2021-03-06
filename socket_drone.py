#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Rafael Figueroa
"""

import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math

# information is passed to the ground station using sockets
import socket

class Socket_drone(object):

    def __init__(self):
        # --- Socket configuration ---
        print 'Connecting to ground station'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1.0)
        self.sock.connect(('192.168.1.10', 50007))
        print 'Connected to ground station'

    def send_data(self, msg):
        fusionPose = msg
        fus_msg = "r:%f p:%f y:%f \0" % (fusionPose[0], 
        fusionPose[1], fusionPose[2])
        # Information sent through socket to gnd station
        self.sock.sendall(fus_msg)

    def close_socket(self):
        self.sock.close()
