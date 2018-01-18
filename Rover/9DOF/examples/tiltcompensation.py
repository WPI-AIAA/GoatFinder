from __future__ import print_function

import Adafruit_LSM9DS0
import math
from itertools import permutations
import time
from tabulate import tabulate

# Create new LSM9DS0 instance
imu = Adafruit_LSM9DS0.LSM9DS0()

table = []

while True:
	(mag_x, mag_y, mag_z) = imu.readMag()
	(acc_x, acc_y, acc_z) = imu.readAccel()

	# Normalising the accelerometer data
	# Dividing variable (don't know why I use this)
	acc_norm_div = math.sqrt(acc_x**2 + acc_y**2 + acc_z**2)

	# Normalised values
	acc_x_norm = acc_x / acc_norm_div
	acc_y_norm = acc_y / acc_norm_div

	# Calc pitch and roll using trig
	pitch = math.asin(acc_x_norm)
	roll = - math.asin(math.radians(acc_y_norm / math.cos(pitch)))

	# Do some mathsy stuff to compensate for the tilt
	mag_x_comp = mag_x * math.cos(pitch) + mag_z * math.sin(pitch)
	mag_y_comp = mag_x * math.sin(roll) * math.sin(pitch) + mag_y * math.cos(roll) - mag_z * math.sin(roll) * math.cos(pitch)

	# Calculate the angle in degrees
	angle_deg = math.degrees(math.atan2(mag_y_comp, mag_x_comp))

	# Work out as a bearing
	if angle_deg < 0:
		angle_deg += 360

	print("Tilt accounted: deg:", angle_deg)

	time.sleep(0.05)





