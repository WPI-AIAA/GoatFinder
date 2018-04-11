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

#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
usingPCB = True

if usingPCB:
    __leftMotor__ = (9,10,8)
    __rightMotor__ = (11,7,14)
    __marker1Servo__ = ("PWM")
    __marker2Servo__ = ("PWM")
    __parachuteServo__ = ("PWM")

    #do other things
else:
    __leftMotor__ = (24,12,8)
    __rightMotor__ = (23,15,14)
    __marker1Servo__ = ("PWM")
    __marker2Servo__ = ("PWM")
    __parachuteServo__ = ("PWM")
