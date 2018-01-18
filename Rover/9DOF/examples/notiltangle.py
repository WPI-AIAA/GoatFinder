# Simple example whereby the angle is calculated, assuming the magnetometer is flat,
# i.e. there is no tilt-compensation.
# Author: Jack Weatherilt
# License: Public Domain
import math
import time

# Import the LSM9DS0 module
import Adafruit_LSM9DS0

# Create new LSM9DS0 instance
imu = Adafruit_LSM9DS0.LSM9DS0()

while True:
	# Unpack (x, y, z) readings from magnetometer 
	(mag_x, mag_y, mag_z) = imu.readMag()

	# Calculate the angle using trigonometry
	angle_deg = math.degrees(math.atan2(mag_y, mag_x))

	# NOTE: this method does not account for tilt!
	print("Non-tilt: deg:", angle_deg)

	# Wait half a second before repeating 
	time.sleep(0.05)





