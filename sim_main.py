#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Rafael Figueroa
Ground Station 
"""

import sys
from time import sleep
from gui_ground import GUI_quad
from model_quad import quad_dynamics
import numpy as np
from collections import namedtuple

# Script
GUI = GUI_quad()

State = namedtuple('State', ['x', 'y', 'z', 'roll', 'pitch', 'yaw',
                   'dx', 'dy', 'dz', 'droll', 'dpitch', 'dyaw'])
Input = namedtuple('Input', ['w1', 'w2', 'w3', 'w4'])
Pose = namedtuple('Pose', ['x', 'y', 'z', 'roll', 'pitch', 'yaw'])

X = State(x = 0.0, y = 0.0, z = 0.0, roll = 0.0, pitch = 0.0, yaw = 0.0,
         dx = 0.0, dy = 0.0, dz = 0.0,
         droll = 0.0, dpitch = 0.0, dyaw = 0.0)

u = Input(w1 = 3000.0, w2 = 3000.0, w3 = 3000.0, w4 = 3000.0)

while True:
    try:        
        q = Pose(x = X.x, y = X.y, z = X.z,
                 roll = X.roll, pitch = X.pitch, yaw = X.yaw)

        GUI.set_pose(q)
        GUI.update_gui()
        X = State._make(quad_dynamics(X, u))

    except KeyboardInterrupt:
        print 'closing all'
        GUI.app.closeAllWindows()
        print 'quitting Qt App'
        GUI.app.quit()
        print 'quitting sim loop'
        break

sys.exit(0)
        
