#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import numpy as np
import shelve

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=False)

pulseMin = 1735  # Min pulse length out of 4096
pulseLow = 2500
pulseMax = 3047
pulseStop = 0

motorChannel = 2

pwm.setPWMFreq(400)                        # Set frequency to x Hz
pwm.setPWM(motorChannel, 0, pulseMin)  # Set to min (thrtle down)
time.sleep(2)  # Wait for motors to be armed

drone_vars = shelve.open('drone_vars')
low_pulse = drone_vars['low_pulse']
high_pulse = drone_vars['high_pulse']
m = (int(high_pulse)-int(low_pulse))/float(8000-3000)
b = float(low_pulse) - m * 3000.0
print 'm', m, 'b', b

try:
    while True:
        rpm_input = input('Provide desired rpm:')
        pulse_input = float(rpm_input)* m + b
        print 'pulse_input:', pulse_input

        if pulse_input > pulseMin and pulse_input < pulseMax:
            pwm.setPWM(motorChannel, 0, int(pulse_input))
        else:
            print 'pulse input wrong range', pulse_input
            pwm.setPWM(motorChannel, 0, pulseStop)
            drone_vars.close()
            break

 # Catch an interrupt and set the motor to stop
except KeyboardInterrupt:
    pwm.setPWM(motorChannel, 0, pulseStop)
    drone_vars.close()
    print('Stopping motor')

