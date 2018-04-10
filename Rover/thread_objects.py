from LSM9DS0 import LSM9DS0
import time
from nav_loader import nav

class hall_thread:
    pass

class nine_dof_thread():
    #global nav
    def __init__(self,t=0.05):
        lsm = LSM9DS0()
        while True:

            nav.new_9dof((lsm.readGyro(),lsm.readMag(),lsm.readAccel()))
            time.sleep(1)
