#Predefined globals for input/output

#replace strings with actual locations

'''
__genericAsyncSerial__ = ("TX","RX")
__genericI2C__ = ("SDA","SCL")
__genericSPI__ = ("MISO","MOSI","SCK")
__genericSPIDevice__ = ("CS")
__genericServo__ = ("PWM")
__genericMotor__ = ("A","B","PWM")
'''

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
usingPCB = True

if usingPCB:
    __leftMotor__ = (14,11,20)
    __rightMotor__ = (13,12,21)
    __marker1Servo__ = ("PWM")
    __marker2Servo__ = ("PWM")
    __parachuteServo__ = ("PWM")

    #do other things
else:
    __leftMotor__ = (14,11,20)
    __rightMotor__ = (13,12,21)
    __marker1Servo__ = ("PWM")
    __marker2Servo__ = ("PWM")
    __parachuteServo__ = ("PWM")
