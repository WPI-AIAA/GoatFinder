#sue me

import inputOutputMacro as iom
import RPI.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(iom.__leftMotor__[0], GPIO.OUT)
GPIO.setup(iom.__leftMotor__[1], GPIO.OUT)
leftmotorPWM = GPIO.PWM(iom.__leftMotor__[2], 100)
leftmotorPWM.start(0)

GPIO.setup(iom.__rightMotor__[0], GPIO.OUT)
GPIO.setup(iom.__rightMotor__[1], GPIO.OUT)
rightmotorPWM = GPIO.PWM(iom.__rightMotor__[2], 100)
rightmotorPWM.start(0)

def startmotors():
    leftmotorPWM.start(0)
    rightmotorPWM.start(0)

def stopmotors():
    leftmotorPWM.stop()
    rightmotorPWM.stop()

def driveleftmotor(velocity):
    if velocity > 1.0:
        velocity = 1.0
    if velocity < -1.0:
        velocity = -1.0

    if velocity > 0:
        GPIO.output(iom.__leftMotor__[0], True)
        GPIO.output(iom.__leftMotor__[1], False)
        leftmotorPWM.ChangeDutyCycle(100*velocity)
    else:
        GPIO.output(iom.__leftMotor__[0], False)
        GPIO.output(iom.__leftMotor__[1], True)
        leftmotorPWM.ChangeDutyCycle(-100*velocity)
        
def driverightmotor(velocity):
    if velocity > 1.0:
        velocity = 1.0
    if velocity < -1.0:
        velocity = -1.0

    if velocity > 0:
        GPIO.output(iom.__rightMotor__[0], True)
        GPIO.output(iom.__rightMotor__[1], False)
        rightmotorPWM.ChangeDutyCycle(100*velocity)
    else:
        GPIO.output(iom.__rightMotor__[0], False)
        GPIO.output(iom.__rightMotor__[1], True)
        rightmotorPWM.ChangeDutyCycle(-100*velocity)
        
