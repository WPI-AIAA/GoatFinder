# Simple test printing the gyroscope, magnetometer and accelerometer values
# every half second.
# Author: Jack Weatherilt
# License: Public Domain
import time

# Import the LSM9DS0 module
import Adafruit_LSM9DS0


# Create new LSM9DS0 instance
imu = Adafruit_LSM9DS0.LSM9DS0()

# Alternatively, you can specify the I2C bus to use:
#imu = Adafruit_LSM9DS0.LSM9DS0(busnum=2) 

print("Printing gyroscope, magnetometer and accelerometer values... Press Ctrl-C to quit.")
while True:
    # Grab (x, y, z) readings for gyro, mag and accelerometer
    gyro, mag, accel = imu.read()

    # Unpack tuples
    gyro_x, gyro_y, gyro_z = gyro
    mag_x, mag_y, mag_z = mag
    accel_x, accel_y, accel_z = accel

    # Print sets of values in separate lines
    print('Gyro:', 'x=', gyro_x, 'y=', gyro_y, 'z=', gyro_z)
    print('Mag:', 'x=', mag_x, 'y=', mag_y, 'z=', mag_z)
    print('Accel:', 'x=', accel_x, 'y=', accel_y, 'z=', accel_z)

    # Wait half a second before repeating
    time.sleep(0.5)

