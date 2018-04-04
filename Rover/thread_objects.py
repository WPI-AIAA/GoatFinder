import LSM9DS0
class hall_thread:j
    pass

class ninedof_thread:
    global nav
    nav.new_9dof((LSM9DS0.readGyro(),LSM9DS0.readMag(),LSM9DS0.readAccel()))
    pass
