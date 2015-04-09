#!/usr/bin/python

import shelve
import matplotlib.pyplot as plt
import numpy as np

drone_vars = shelve.open('drone_vars')
print drone_vars

rpm_vals = [x*1000 for x in range(3, 9)]
pulse_vals = [drone_vars[str(x)] for x in rpm_vals]
print rpm_vals, pulse_vals
plt.plot(rpm_vals, pulse_vals, label = 'test')

poly_coef = np.polyfit(np.array(rpm_vals), np.array(pulse_vals), 2)
poly_fitted = np.poly1d(poly_coef)
plt.plot(rpm_vals, [poly_fitted(x) for x in rpm_vals], label = 'fit')



plt.xlabel('RPM')
plt.ylabel('PWM pulse width percent = value/4096')
plt.legend(['test', 'fit'])
plt.tight_layout()
plt.savefig('/home/rafa/gitcode/drone/figures/MotorPWMtoRPM.png')
