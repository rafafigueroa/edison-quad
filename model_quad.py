#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Rafael Figueroa
Derivation of Rotation Matrix
"""

from __future__ import division
import numpy as np
from sympy import *
from robot_vars import m

def Rx(h):
    return np.array([[1, 0, 0],
                     [0, cos(h), -sin(h)],
                     [0, sin(h), cos(h)]])

def Ry(h):
    return np.array([[cos(h), 0, sin(h)],
                     [0, 1, 0],
                     [-sin(h), 0, cos(h)]])

def Rz(h):
    return np.array([[cos(h), -sin(h), 0],
                     [sin(h), cos(h), 0],
                     [0, 0, 1]])


def Rzyx(hx, hy, hz):
    """ Rzyx = Rz(hz) * Ry(hy) * Rx(hx) """
    return np.array(
        [[ cos(hy)*cos(hz), cos(hz)*sin(hx)*sin(hy) - cos(hx)*sin(hz), sin(hx)*sin(hz) + cos(hx)*cos(hz)*sin(hy)],
        [ cos(hy)*sin(hz), cos(hx)*cos(hz) + sin(hx)*sin(hy)*sin(hz), cos(hx)*sin(hy)*sin(hz) - cos(hz)*sin(hx)],
        [        -sin(hy),                           cos(hy)*sin(hx),                           cos(hx)*cos(hy)]])

def quad_dynamics(x, y, z, hx, hy, hz, 
                  dx, dy, dz, dhx, dhy, dhz, 
                  T, w1, w2, w3, w4):
    
    ddx = (T/m) * (sin(hx)*sin(hz) + cos(hx)*cos(hz)*sin(hy)) 
    ddy = (T/m) * (cos(hx)*sin(hy)*sin(hz) - cos(hz)*sin(hx))
    ddz = (T/m) * cos(hx)*cos(hy) - g


print Rzyx(0, 0, 0)
print Rzyx(np.pi, 0, 0)
print Rzyx(0, np.pi, 0)
print Rzyx(0, 0, np.pi)

