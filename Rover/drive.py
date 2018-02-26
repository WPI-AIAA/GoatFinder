import math
from PIDcontrol import PID
import matplotlib.pyplot as plt


direction = 0.0

deltadir = [0.0,0.0]

oldmotorspeed = [0.0,0.0]
oldturnamt = 0.0

inertia = 0.9


def turn(motorspeed):
    global direction
    
    global oldturnamt
    global inertia
    
    turnamt = (motorspeed[0] - motorspeed[1])/5
    turnamt = turnamt*(1-inertia) + oldturnamt*inertia
    oldturnamt = turnamt
    direction += turnamt

def updatewheel(motorspeed):
    global deltadir

    global oldmotorspeed
    global inertia
    
    motorspeed[0] = motorspeed[0]*(1-inertia) + oldmotorspeed[0]*inertia
    motorspeed[1] = motorspeed[1]*(1-inertia) + oldmotorspeed[1]*inertia
    oldmotorspeed[0] = motorspeed[0]
    oldmotorspeed[1] = motorspeed[1]
    
    deltadir[0] = motorspeed[0]/10
    deltadir[1] = motorspeed[1]/10

#drive program, uses PID controller and function inputs
def compass():
    #placeholder. determines direction the rover is facing (CW, 0 at y-up)
    return direction
def wheeltravel():
    #placeholder. determines distance the rover has traveled since the last update
    return deltadir

def iscloseenough(tgtlocation, location, margin):
    dispx = tgtlocation[0] - location[0]
    dispy = tgtlocation[1] - location[1]
    if dispx < margin and -dispx < margin and dispy < margin and -dispy < margin:
        return True
    return False
    
def drive(tgtlocation, location):
    while not iscloseenough(tgtlocation, location, 0.05): #we should determine what the correct 
        #tgtlocation and location are arrays with x and y-distances
        dircontroller = PID(1.5,1,1.5,.5)
        speedcontroller = PID(1,0,0,.5)
        
        direction = compass()
        delta = wheeltravel()
        
        speed = math.sqrt(math.pow(delta[0],2)+math.pow(delta[1],2))
        delta = [math.cos(direction)*(delta[0]+delta[1])/2,math.sin(direction)*(delta[0]+delta[1])/2]

        location[0] += delta[0]
        location[1] += delta[1]

        distanceleft = [tgtlocation[0]-location[0],tgtlocation[1]-location[1]]

        direction = math.atan2(distanceleft[1], distanceleft[0])
        distance = math.sqrt(math.pow(distanceleft[0],2)+math.pow(distanceleft[1],2))

        if speed == 0:
                    speed = 0.01

        tgtspeed = speedcontroller.update(distance) #optimal speed for rover to travel at

        turnerror = direction - compass()

        if turnerror > math.pi:
            turnerror = 2*math.pi - turnerror
        if turnerror < -math.pi:
            turnerror = turnerror + 2*math.pi
        
        tgtdirection = dircontroller.update(turnerror) #amount for rover to turn CW

        if tgtspeed > 1:
                        tgtspeed = 1.0

        motorspeed = [tgtspeed+tgtdirection,tgtspeed-tgtdirection]
        if motorspeed[0] > motorspeed[1]:
            motorspeed = [1.0,motorspeed[1]/motorspeed[0]]
        else:
            motorspeed = [motorspeed[0]/motorspeed[1],1.0]
        motorspeed = [motorspeed[0]*tgtspeed, motorspeed[1]*tgtspeed]
        #TODO: write values to motor

        motorspeed[1] = motorspeed[1]*1.0

        if __name__ == '__main__': #this is for debug purposes

            #print("---")
            #print(motorspeed[0])
            #print(motorspeed[1])
            #print(direction)
            
            turn(motorspeed)
            updatewheel(motorspeed)
            plt.scatter(location[0],location[1])
            #plt.pause(0.01)

if __name__ == '__main__':
    drive([-2,2],[0,0])
    drive([-2,-2],[-2,2])
    drive([.5,0],[-2,-2])
    plt.show()
