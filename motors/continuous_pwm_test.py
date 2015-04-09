#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import numpy as np

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=False)

servoMin = 1735  # Min pulse length out of 4096
servoLow = 2000
servoMax = 3047
servoStop = 0

motorChannel = 0

def setServoPulse(channel, pulse):
    pulseLength = 1000000                   # 1,000,000 us per second
    pulseLength /= 60                       # 60 Hz
    print "%d us per period" % pulseLength
    pulseLength /= 4096                     # 12 bits of resolution
    print "%d us per bit" % pulseLength
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(400)                        # Set frequency to x Hz
pwm.setPWM(motorChannel, 0, servoMin)  # Set to min (thrtle down)
time.sleep(1)  # Wait for motors to be armed

pwmTestValues = np.linspace(servoMin, servoMax, num=101).astype(int) 
print 'pwmTestValues', pwmTestValues

try:
    while True:
        # Change speed of continuous servo on channel O
        for pwmVal in pwmTestValues: 
            pwmPercent = int(100*(pwmVal-servoMin)/float(servoMax-servoMin))
            print 'percent:', pwmPercent, 'rpm:', pwmPercent*12*850/100.0
            pwm.setPWM(motorChannel, 0, pwmVal)
            time.sleep(2)

 # Catch an interrupt and set the motor to stop
except KeyboardInterrupt:
    pwm.setPWM(motorChannel, 0, servoStop)
    print('Stopping motor')





