#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Rafael Figueroa
Ground Station 
"""

from time import sleep
from gui_main import GUI_quad
import numpy as np
    
# Script
GUI = GUI_quad()

for a in range(0, 100):
    
    X = np.array([0, 0, 0, np.pi/(a+4.0), 0, np.pi/2.0])
    GUI.set_state(X)
    GUI.update_gui()
    sleep(0.1)

