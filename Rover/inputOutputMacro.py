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

usingPCB = True

if usingPCB:
    __leftMotor__ = ("A","B","PWM")
    __rightMotor__ = ("A","B","PWM")
    __marker1Servo__ = ("PWM")
    __marker1Servo__ = ("PWM")
    __parachuteServo__ = ("PWM")

    #do other things
else:
    __leftMotor__ = ("A","B","PWM")
    __rightMotor__ = ("A","B","PWM")
    __marker1Servo__ = ("PWM")
    __marker1Servo__ = ("PWM")
    __parachuteServo__ = ("PWM")
