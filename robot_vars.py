#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Rafael Figueroa
Static Variables
"""

m = 0.5  # Kg TODO: find for my drone
L = 0.175 # m TODO: find for my drone
g = 9.81 # m/(s^2)
kF = 1.4193491613e-07 # N/(rpm^2)
kM = 1.5e-9 # N*m/(rpm^2) TODO: find for my drone

# Inertias, recalculate inverses

Ixx = 0.00232 # kg/(m^2) TODO: find for my drone
Iyy = 0.00232
Izz = 0.00400

