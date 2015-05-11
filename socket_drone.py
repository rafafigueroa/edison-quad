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
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1.0)
        self.sock.connect(('192.168.0.10', 50007))

    def send_data(self, msg):
        fusionPose = msg
        fus_msg = "r: %f p: %f y: %f" % (math.degrees(fusionPose[0]), 
        math.degrees(fusionPose[1]), math.degrees(fusionPose[2]))
        # Information sent through socket to gnd station
        sock.sendall(fus_msg)

    def close_socket(self):
        sock.close()
