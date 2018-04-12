import math
from PIDcontrol import PID
import motorOutput as mot
import nav_loader 
import time

def iscloseenough(tgtlocation, location, margin):
    dispx = tgtlocation[0] - location[0]
    dispy = tgtlocation[1] - location[1]
    if dispx < margin and -dispx < margin and dispy < margin and -dispy < margin:
        return True
    return False
#global nav

def turn(tgtheading):

    dircontroller = PID(1.5,1,2.5)
    global nav_loader

    #heading = nav_loader.heading
    _,_,heading,_ = nav_loader.nav.read_displacement()

    while not (tgtheading - heading) < .017:
        time.sleep(.1)

        #heading = nav_loader.heading
        _,_,heading,_ = nav_loader.nav.read_displacement()

        error = tgtheading - heading

        if error > math.pi:
            error = 2*math.pi - error
        if error < -math.pi:
            error = error + 2*math.pi

        wheel = dircontroller.update(error)

        if wheel > 1:
            wheel = 1.0

        mot.driveleftmotor(wheel)
        mot.driverightmotor(-wheel)
    mot.stopmotors()
    time.sleep(0.5)
    #set accelerometer to 0 velocity
        
    
def drive(tgtlocation, location):

    dircontroller = PID(1.5,1,2.5)
    speedcontroller = PID(1,0,0)
    #mot.startmotors()
    
    while not iscloseenough(tgtlocation, location, 0.5): #we should determine what the correct 
        time.sleep(.1)
        #tgtlocation and location are [y,x] arrays
        
        #direction = compass()
        #delta = wheeltravel()
        # TODO FIX THIS SHIT NATHAN
        # TODONE I THINK
        global nav_loader
        #print(nav_loader.nav)
        #dx = nav_loader.x
        #dy = nav_loader.y
        #heading = nav_loader.heading
        #print("heading:")
        #print(heading)
        #print("x/y")
        #print((dx,dy))
        #nav_loader.x = 0
        #nav_loader.y = 0
        #print(dx)
        #print(dy)
        dx, dy, heading,_ = nav_loader.nav.read_displacement()
        
        speed = math.sqrt(math.pow(dx,2)+math.pow(dy,2))
        #delta = [math.cos(direction)*(delta[0]+delta[1])/2,math.sin(direction)*(delta[0]+delta[1])/2]

        location[0] += dy
        location[1] += dx

        distanceleft = [tgtlocation[0]-location[0],tgtlocation[1]-location[1]]

        tgtdirection = math.atan2(distanceleft[1], distanceleft[0])
        distance = math.sqrt(math.pow(distanceleft[0],2)+math.pow(distanceleft[1],2))

        if speed == 0:
                    speed = 0.01

        tgtspeed = speedcontroller.update(distance) #optimal speed for rover to travel at

        turnerror = tgtdirection - heading

        if turnerror > math.pi:
            turnerror = 2*math.pi - turnerror
        if turnerror < -math.pi:
            turnerror = turnerror + 2*math.pi
        
        tgtdirection = dircontroller.update(turnerror) #amount for rover to turn CW

        if tgtdirection > 1:
            tgtdirection = 1.0
        elif tgtdirection < -1:
            tgtdirection = -1.0

        if tgtspeed > 1:
            tgtspeed = 1.0
        elif tgtspeed < 0.3:
            tgtspeed = 0.3

        motorspeed = [tgtspeed+tgtdirection,tgtspeed-tgtdirection]
        if motorspeed[0] > motorspeed[1]:
            motorspeed = [1.0,motorspeed[1]/motorspeed[0]]
        else:
            motorspeed = [motorspeed[0]/motorspeed[1],1.0]
        motorspeed = [motorspeed[0]*tgtspeed, motorspeed[1]*tgtspeed]

        print("Motor speeds:")
        print(motorspeed)
        mot.driveleftmotor(motorspeed[0])
        mot.driverightmotor(motorspeed[1])

    mot.stopmotors()
    time.sleep(0.5)
    #set accelerometer to 0 velocity

if __name__ == '__main__':
    drive([-2,2],[0,0])
    drive([-2,-2],[-2,2])
    drive([.5,0],[-2,-2])
    #plt.show()
