from LSM9DS0 import LSM9DS0
import time
import nav_loader

class hall_thread:
    pass

class nine_dof_thread():
    def __init__(self,t=0.05):
        #global nav
        lsm = LSM9DS0()
        global nav_loader
        print(nav_loader.nav)
        while True:
            #nav_loader.nav.new_9dof((lsm.readGyro(),lsm.readMag(),lsm.readAccel()))
            data = (lsm.readGyro(),lsm.readMag(),lsm.readAccel())
            #print(data)
            nav_loader.nav.new_9dof(data)

            x_l, y_l, nav_loader.heading, skid = nav_loader.nav.read_displacement()
            nav_loader.x += x_l
            nav_loader.y += y_l

            

            #print(nav_loader.nav)
            #print(nav_loader.nav.accel)
            time.sleep(.05)

