import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math

# information is passed to the ground station using sockets
import socket

SETTINGS_FILE = "RTIMULib"

print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
    print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

print("IMU Name: " + imu.IMUName())

if (not imu.IMUInit()):
    print("IMU Init Failed");
    sys.exit(1)
else:
    print("IMU Init Succeeded");

poll_interval = imu.IMUGetPollInterval()
print("Recommended Poll Interval: %dmS\n" % poll_interval)

# --- Socket configuration ---

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1.0)
sock.connect(('192.168.0.10', 50007))

# --- Loop ---
while True:
    if imu.IMURead():
        # x, y, z = imu.getFusionData()
        # print("%f %f %f" % (x,y,z))
        data = imu.getIMUData()
        fusionPose = data["fusionPose"]
        fus_msg = "r: %f p: %f y: %f" % (math.degrees(fusionPose[0]), 
        math.degrees(fusionPose[1]), math.degrees(fusionPose[2]))
        print(fus_msg)

        # Information sent through socket to gnd station
        sock.sendall(fus_msg)
        time.sleep(poll_interval*1.0/1000.0)

sock.close()
