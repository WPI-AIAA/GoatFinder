# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
#pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
pwm = Adafruit_PCA9685.PCA9685(address=0x70, busnum=1)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

motor_min = 0
motor_max = 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    #print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    #print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)


#0-100 because that's what the RPi GPIO library uses
def set_leftmotor(pulse):
    pulse = (pulse*(motor_min-motor_max)/100)+motor_min
    pwm.set_pwm(0,0,int(pulse))
def set_rightmotor(pulse):
    pulse = (pulse*(motor_min-motor_max)/100)+motor_min
    pwm.set_pwm(1,0,int(pulse))
def set_dropper1(pulse):
    pulse = (pulse*(servo_min-servo_max)/100)+servo_min
    pwm.set_pwm(2,0,int(pulse))
def set_dropper2(pulse):
    pulse = (pulse*(servo_min-servo_max)/100)+servo_min
    pwm.set_pwm(3,0,int(pulse))
def set_dropper3(pulse):
    pulse = (pulse*(servo_min-servo_max)/100)+servo_min
    pwm.set_pwm(4,0,int(pulse))


#print('Moving servo on channel 0, press Ctrl-C to quit...')
#while True:
    # Move servo on channel O between extremes.
#    pwm.set_pwm(0, 0, servo_min)
#    time.sleep(1)
#    pwm.set_pwm(0, 0, servo_max)
#    time.sleep(1)

if __name__ == '__main__':
    while True:
        for i in range(0, 100):
            set_dropper1(i)
            time.sleep(.5)
        for i in range(0, 100):
            set_dropper1(100-i)
            time.sleep(.5)
        




