from LSM9DS0 import LSM9DS0
import time
import nav_loader
from math import isnan

class hall_thread:
    pass

def nine_dof_thread(t=0.05):
    #global nav
    lsm = LSM9DS0()
    global nav_loader
    print(nav_loader.nav)
    while True:
        #nav_loader.nav.new_9dof((lsm.readGyro(),lsm.readMag(),lsm.readAccel()))
        data = (lsm.readGyro(),lsm.readMag(),lsm.readAccel())
        #print(data)
        nav_loader.nav.new_9dof(data)

        x_l, y_l, heading, skid = nav_loader.nav.read_displacement()
        print("heading as reported immediately")
        print(heading)

        if not isnan(x_l) and not isnan(y_l) and not isnan(heading):
            nav_loader.x += x_l
            nav_loader.y += y_l
            nav_loader.heading = heading 

        

        #print(nav_loader.nav)
        #print(nav_loader.nav.accel)
        time.sleep(.05)

