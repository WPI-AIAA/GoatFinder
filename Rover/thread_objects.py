import LSM9DS0
import time
class hall_thread:
    pass

class ninedof_thread(t=0.05):
    global nav
    def __init__():
        while True:
            nav.new_9dof((LSM9DS0.readGyro(),LSM9DS0.readMag(),LSM9DS0.readAccel()))
            time.sleep(t)
