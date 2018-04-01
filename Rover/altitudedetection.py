import time

initialalt = 0

altmargin = 10
statmargin = 5

deltat = 1

def getalt():
    #preferably in meters
    return 0


def initializealt():
    #waits for pressure readings to stabilize (might not be necessary)
    global initialalt

    isstationary()

    #records initial altitude
    initialalt = getpressure()
        
def isstationary():
    global deltat
    global altmargin
    alt = getalt()
    while not count >= statmargin:
        time.sleep(deltat)
        oldalt = alt
        alt = getalt()
        slope = (alt - oldalt)/deltat
        if slope < 0:
            slope = -slope
        if slope < altmargin:
            count += 1

def ismovingup():
    global deltat
    global altmargin
    global initialalt
    alt = getalt()
    while not count >= statmargin:
        time.sleep(deltat)
        oldalt = alt
        alt = getpressure()
        slope = (alt - oldalt)/deltat
        if slope > altmargin:
            count += 1
        if alt > initialalt + 150:
            count = statmargin
    
def ismovingdown():
    global deltat
    global altmargin
    global initialalt
    alt = getalt()
    while not count >= statmargin:
        time.sleep(deltat)
        oldalt = alt
        alt = getpressure()
        slope = (alt - oldalt)/deltat
        if slope < altmargin/2:
            count += 1
        if alt < initialalt + 150:
            count = statmargin
