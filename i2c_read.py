#!/usr/bin/python

import smbus
I2C_ADDRESS = 0x6b
bus = smbus.SMBus(1)
value = bus.read_byte(I2C_ADDRESS)
print "%02X" % value

