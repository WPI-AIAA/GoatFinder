#boi he bout to do it

import pwmHelper as pwmH
import time

OPEN = 100
CLOSED = 0

def grabparachute():
    pwmH.set_dropper1(CLOSED)
def releaseparachute():
    pwmH.set_dropper1(OPEN)
    time.sleep(2)

def setupdroppers():
    pwmH.set_dropper2(CLOSED)
    pwmH.set_dropper3(CLOSED)
    time.sleep(2)

def dropfirst():
    pwmH.set_dropper2(OPEN)
    time.sleep(2)

def dropsecond():
    pwmH.set_dropper3(OPEN)
    time.sleep(2)
