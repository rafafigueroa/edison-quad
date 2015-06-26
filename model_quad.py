#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Rafael Figueroa
Derivation of Rotation Matrix
"""

from __future__ import division
import numpy as np
from sympy import *
from robot_vars import *

def minAngle(ang):
    return np.arctan2(np.sin(ang), np.cos(ang))

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
    """ From ETH, Flying Inverted Pendulum
        Rzyx = Rz(hz) * Ry(hy) * Rx(hx)
        Rzyx = Rz(yaw) * Ry(pitch) * Rx(roll)"""
    return np.array(
        [[ cos(hy)*cos(hz), cos(hz)*sin(hx)*sin(hy) - cos(hx)*sin(hz), sin(hx)*sin(hz) + cos(hx)*cos(hz)*sin(hy)],
        [ cos(hy)*sin(hz), cos(hx)*cos(hz) + sin(hx)*sin(hy)*sin(hz), cos(hx)*sin(hy)*sin(hz) - cos(hz)*sin(hx)],
        [        -sin(hy),                           cos(hy)*sin(hx),                           cos(hx)*cos(hy)]])

def quad_dynamics(X, u):
    """ From UAV Handbook
        Rotation is ZXY """

    x, y, z, roll, pitch, yaw, dx, dy, dz, droll, dpitch, dyaw = X
    w1, w2, w3, w4 = u

    T1 = kF*w1**2
    T2 = kF*w2**2
    T3 = kF*w3**2
    T4 = kF*w4**2

    T = T1 + T2 + T3 + T4
    
    # Second derivatives of
    ddx = (T/m) * (sin(roll)*sin(yaw) + cos(roll)*cos(yaw)*sin(pitch)) 
    ddy = (T/m) * (cos(roll)*sin(pitch)*sin(yaw) - cos(yaw)*sin(roll))
    ddz = (T/m) * cos(roll)*cos(yaw) - g

    # Angular velocities with respect to body frame
    nx = droll*cos(pitch) - dyaw*cos(roll)*sin(pitch)
    ny = dpitch + dyaw*sin(roll)
    nz = droll*sin(pitch) + dyaw*cos(roll)*cos(pitch)

    # First derivatives of velocities with respect to body frame
    dnx = L*(T2-T4)/Ixx + (ny*nz*(Izz - Iyy))/Ixx
    dny = L*(T3-T1)/Iyy + (nx*nz*(Ixx - Izz))/Iyy
    dnz = L*kM*(T1-T2+T3-T4)/Izz + (nx*ny*(Iyy - Ixx))/Izz

    # Integration, xa means x after
    Ts = 0.01

    xa = x + Ts*dx
    ya = y + Ts*dy
    za = z + Ts*dz

    dxa = dx + Ts*ddx
    dya = dy + Ts*ddy
    dza = dz + Ts*ddz

    rolla = minAngle(roll + Ts*droll)
    pitcha = minAngle(pitch + Ts*dpitch)
    yawa = minAngle(yaw + Ts*dyaw)

    nxa = nx + Ts*dnx
    nya = ny + Ts*dny
    nza = nz + Ts*dnz

    drolla = cos(pitcha)*nxa + sin(pitcha)*nza
    dpitcha = (sin(pitcha)*sin(rolla)/cos(rolla))*nxa + nya \
              -(cos(pitcha)*sin(rolla)/cos(rolla))*nza
    dyawa = -(sin(pitcha)/cos(rolla))*nxa + (cos(pitcha)/cos(rolla))*nza

    # Return state after integration

    return tuple(float(val) for val in (xa, ya, za, rolla, pitcha, yawa, 
           dxa, dya, dza, drolla, dpitcha, dyawa))

#print Rzyx(0, 0, 0)
#print Rzyx(np.pi, 0, 0)
#print Rzyx(0, np.pi, 0)
#print Rzyx(0, 0, np.pi)

