from LSM9DS0 import LSM9DS0
import time
from nav_loader import nav

class hall_thread:
    pass

class nine_dof_thread():
    #global nav
    def __init__(t=0.05):
        while True:
            lsm = LSM9DS0()

            nav.new_9dof((lsm.readGyro(),lsm.readMag(),lsm.readAccel()))
            time.sleep(t)
