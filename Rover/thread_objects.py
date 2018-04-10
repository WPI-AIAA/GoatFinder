import LSM9DS0
import time
from nav_loader import nav

class hall_thread:
    pass

class nine_dof_thread():
    #global nav
    def __init__(t=0.05):
        while True:
            nav.new_9dof((LSM9DS0.readGyro(),LSM9DS0.readMag(),LSM9DS0.readAccel()))
            time.sleep(t)
