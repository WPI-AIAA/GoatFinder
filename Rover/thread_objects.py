from LSM9DS0 import LSM9DS0
import time
import nav_loader

class hall_thread:
    pass

class nine_dof_thread():
    def __init__(self,t=0.05):
        #global nav
        lsm = LSM9DS0()
        print(nav_loader.nav)
        while True:
            #nav_loader.nav.new_9dof((lsm.readGyro(),lsm.readMag(),lsm.readAccel()))
            data = (lsm.readGyro(),lsm.readMag(),lsm.readAccel())
            #print(data)
            nav_loader.nav.new_9dof(data)
            time.sleep(.05)

