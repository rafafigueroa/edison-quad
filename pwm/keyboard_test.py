#!/usr/bin/python

import curses
import shelve

from Adafruit_PWM_Servo_Driver import PWM
import time
import numpy as np

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=False)

pwmMin = 1735  # Min pulse length out of 4096
pwmLow = 2500
pwmMax = 3047
pwmStop = 0

motorChannel = 0
pwm.setPWMFreq(400)                        # Set frequency to x Hz
pwm.setPWM(motorChannel, 0, pwmMin)  # Set to min (thrtle down)
time.sleep(2)  # Wait for motors to be armed

drone_vars = shelve.open('drone_vars')
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0, 10, "Hit 'q' to quit and 'w' to save")
stdscr.addstr(1, 10, "Calibrating High: Up/Down")
stdscr.addstr(2, 10, "Calibrating Low : Left/Right")

stdscr.refresh()

key = ''
pwm_pulse_low = 1735
pwm_pulse_high = 3047

def close_safely():
    drone_vars.close()
    pwm.setPWM(motorChannel, 0, pwmStop)
    curses.endwin()
    print('Stopping motor')

try:
    while key != ord('q'):
        key = stdscr.getch()
        stdscr.refresh()

        if key == curses.KEY_LEFT: 
            pwm_pulse_low = pwm_pulse_low - 1
            stdscr.addstr(6, 20, "LOW 3000rpm:  " + str(pwm_pulse_low))
            pwm.setPWM(motorChannel, 0, pwm_pulse_low)

        elif key == curses.KEY_RIGHT: 
            pwm_pulse_low = pwm_pulse_low + 1
            stdscr.addstr(6, 20, "LOW 3000rpm:  " + str(pwm_pulse_low))
            pwm.setPWM(motorChannel, 0, pwm_pulse_low)

        elif key == curses.KEY_DOWN:
            pwm_pulse_high = pwm_pulse_high - 1
            stdscr.addstr(5, 20, "HIGH 8000rpm: " + str(pwm_pulse_high))
            pwm.setPWM(motorChannel, 0, pwm_pulse_high)

        elif key == curses.KEY_UP:
            pwm_pulse_high = pwm_pulse_high + 1
            stdscr.addstr(5, 20, "HIGH 8000rpm: " + str(pwm_pulse_high))
            pwm.setPWM(motorChannel, 0, pwm_pulse_high)

        elif key == ord('w'):
            stdscr.addstr(8, 20, 'Saving values to file')
            drone_vars['low_pulse'] = pwm_pulse_low
            drone_vars['high_pulse'] = pwm_pulse_high
            close_safely()
        
    close_safely()

# Catch an interrupt and set the motor to stop
except KeyboardInterrupt:
    close_safely()
    
