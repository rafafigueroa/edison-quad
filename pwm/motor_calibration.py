#!/usr/bin/python

import curses
import shelve

from Adafruit_PWM_Servo_Driver import PWM
import time
import numpy as np

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=False)

pulseMin = 1735  # Min pulse length out of 4096
pulseLow = 2500
pulseMax = 3047
pulseStop = 0

motorChannel = 0
pwm.setPWMFreq(400)                    # Set frequency to x Hz
pwm.setPWM(motorChannel, 0, pulseMin)  # Set to min (thrtle down)
time.sleep(2)  # Wait for motors to be armed

drone_vars = shelve.open('drone_vars')
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0, 10, "Hit 'q' to quit, 'j' to go down and 'k' to go up")

stdscr.refresh()

key = ''
pwm_pulse_low = 1735
pwm_pulse_high = 3047

def close_safely():
    drone_vars.close()
    pwm.setPWM(motorChannel, 0, pulseStop)
    curses.endwin()
    print('Stopping motor')

cal_index = 3
pwm_pulse = 2000

try:
    while key != ord('q'):
        key = stdscr.getch()
        stdscr.refresh()
        cal_rpm = cal_index * 1000

        if key == curses.KEY_LEFT: 
            pwm_pulse = pwm_pulse - 1
            stdscr.addstr(cal_index, 20, 'cal rpm: ' + str(cal_rpm)) + \
                                         ' pulse: ' + str(pwm_pulse))
            pwm.setPWM(motorChannel, 0, pwm_pulse)

        elif key == curses.KEY_RIGHT: 
            pwm_pulse = pwm_pulse + 1
            stdscr.addstr(cal_index, 20, 'cal rpm: ' + str(cal_rpm) + \
                                         ' pulse: ' + str(pwm_pulse))
            pwm.setPWM(motorChannel, 0, pwm_pulse)

        elif key == ord('j'):
            stdscr.addstr(cal_index, 20, 'saved rpm: ' + str(cal_rpm) + \
                                         ' pulse: ' + str(pwm_pulse))
            drone_vars[cal_rpm] = pwm_pulse
            cal_index = cal_index + 1
 
        elif key == ord('k'):
            stdscr.addstr(cal_index, 20, 'saved rpm: ' + str(cal_rpm) + \
                                         ' pulse: ' + str(pwm_pulse))
            drone_vars[cal_rpm] = pwm_pulse
            cal_index = cal_index - 1
        
    close_safely()

# Catch an interrupt and set the motor to stop
except KeyboardInterrupt:
    close_safely()
    
