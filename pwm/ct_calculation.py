#!/usr/bin/python

import shelve
import matplotlib.pyplot as plt
import numpy as np

rho = 1.116  # kg/m^3
D = 0.254  # m
b_Ct = rho * D**4  #b over Ct
print 'b/Ct: (kg m)', b_Ct
b_Ct_rpm = b_Ct * (1/60.0)**2
print 'b/Ct: (N/rpm^2)', b_Ct_rpm
b = b_Ct_rpm * 0.11
print 'b: (N/rpm^2)', b
omega_h = np.sqrt(1.2*9.81/float(4*b))
print 'omega_h: rpm', omega_h


