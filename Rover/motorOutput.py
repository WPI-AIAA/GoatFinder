#sue me

import inputOutputMacro as iom
import pwmHelper as pwmH
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(iom.__leftMotor__[0], GPIO.OUT)
GPIO.setup(iom.__leftMotor__[1], GPIO.OUT)
#GPIO.setup(iom.__leftMotor__[2], GPIO.OUT)
#leftmotorPWM = GPIO.PWM(iom.__leftMotor__[2], 100)
#leftmotorPWM.start(0)

GPIO.setup(iom.__rightMotor__[0], GPIO.OUT)
GPIO.setup(iom.__rightMotor__[1], GPIO.OUT)
#GPIO.setup(iom.__rightMotor__[2], GPIO.OUT)
#rightmotorPWM = GPIO.PWM(iom.__rightMotor__[2], 100)
#rightmotorPWM.start(0)

#def startmotors():
    #leftmotorPWM.start(0)
    #rightmotorPWM.start(0)

def stopmotors():
    #leftmotorPWM.stop()
    #rightmotorPWM.stop()
    pwmH.set_leftmotor(0)
    pwmH.set_rightmotor(0)
    GPIO.output(iom.__leftMotor__[0], False)
    GPIO.output(iom.__leftMotor__[1], False)
    GPIO.output(iom.__rightMotor__[0], False)
    GPIO.output(iom.__rightMotor__[1], False)

def driverightmotor(velocity):
    if velocity > 1.0:
        velocity = 1.0
    if velocity < -1.0:
        velocity = -1.0

    if velocity >= 0:
        GPIO.output(iom.__rightMotor__[0], True)
        GPIO.output(iom.__rightMotor__[1], False)
        #leftmotorPWM.ChangeDutyCycle(100*velocity)
        pwmH.set_rightmotor(100*velocity)
        
    else:
        GPIO.output(iom.__rightMotor__[0], False)
        GPIO.output(iom.__rightMotor__[1], True)
        #leftmotorPWM.ChangeDutyCycle(-100*velocity)
        pwmH.set_rightmotor(-100*velocity)
        
def driveleftmotor(velocity):
    if velocity > 1.0:
        velocity = 1.0
    if velocity < -1.0:
        velocity = -1.0

    if velocity >= 0:
        GPIO.output(iom.__leftMotor__[0], True)
        GPIO.output(iom.__leftMotor__[1], False)
        #rightmotorPWM.ChangeDutyCycle(100*velocity)
        pwmH.set_leftmotor(100*velocity)
    else:
        GPIO.output(iom.__leftMotor__[0], False)
        GPIO.output(iom.__leftMotor__[1], True)
        #rightmotorPWM.ChangeDutyCycle(-100*velocity)
        pwmH.set_leftmotor(-100*velocity)
        

if __name__ == '__main__':
    while True:
        for i in range(0,100):
            driveleftmotor(i/200)
            #driverightmotor(i/100)
            time.sleep(.5)
        #for i in range(0,200):
        #    driveleftmotor((100-i)/100)
        #    time.sleep(.5)
        #for i in range(0,100):
        #    driveleftmotor((i-100)/100)
        #    time.sleep(.5)
