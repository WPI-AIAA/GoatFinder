import math
from PIDcontrol import PID
#drive program, uses PID controller and function inputs
def compass():
    #placeholder. determines direction the rover is facing (CW, 0 at y-up)
    return 0.0
def wheeltravel():
    #placeholder. determines distance the rover has traveled since the last update
    return [0.0,0.0]

def drive(tgtlocation, location):
    #tgtlocation and location are arrays with x and y-distances
    dircontroller = PID(1,1,1,.5)
    speedcontroller = PID(1,0,1,.5)
    
    direction = compass()
    delta = wheeltravel()
    delta = [delta[1]*math.sin(direction)-delta[0]*math.cos(direction),delta[1]*math.cos(direction)-delta[0]*math.sin(direction)]

    speed = math.sqrt(math.pow(delta[0],2)+math.pow(delta[1],2))

    location[0] += delta[0]
    location[1] += delta[1]

    distanceleft = [tgtlocation[0]-location[0],tgtlocation[1]-location[1]]

    direction = math.atan2(distanceleft[1], distanceleft[0])
    distance = math.sqrt(math.pow(distanceleft[0],2)+math.pow(distanceleft[1],2))

    tgtspeed = speedcontroller.update(distance/speed) #optimal speed for rover to travel at
    tgtdirection = dircontroller.update(direction) #amount for rover to turn CW

    if tgtspeed > 1:
        tgtspeed = 1

    motorspeed = [tgtspeed+tgtdirection,tgtspeed-tgtdirection]
    if motorspeed[0] > motorspeed[1]:
        motorspeed = [1,motorspeed[1]/motorspeed[0]]
    else:
        motorspeed = [motorspeed[0]/motorspeed[1],1]
    motorspeed = [motorspeed[0]*tgtspeed, motorspeed[1]*tgtspeed]
    #TODO: write values to motor

    

    
