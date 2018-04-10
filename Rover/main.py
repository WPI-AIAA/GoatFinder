
from enum import Enum
import threading
from thread_objects import *
from navSystem_hall import navsystem

class State(Enum):
	TEST = 1
	STANDBY = 2
	ARM = 3

# Initialization
# Run setup and tests

hall_reader = threading.Thread(target = hall_thread, daemon = True)
nine_dof_reader = threading.Thread(target = nine_dof_thread, daemon = True)

nav = navsystem(
        xy_frames_stored = 5,
        sensor_frames_stored = 20,
        encoder_frames_stored = 20,
        zero_angle = 0, # TODO modify this to run parallel to rows of field
        encoder_distance = 2.7474,
        skid_err_range = .5, # TODO adjust based on tests
        accel_time_step = ,# TODO set before running
        gyro_pitch_axis = 1, # Y/1 for PCB
        )



# Go Into Operation Mode
hall_reader.run()
nine_dof_reader.run()


#Nathan's really old stuff (w/ two example functions)
from PIDcontrol import PID
from functionQueue import *
import drive as dr

#testing PID
#controller = PID(1,1,1,.5)

#you can add functions to the queue
addToQueue((dr.drive, [1,1],[0,0]))
addToQueue((dr.drive, [0,0],[1,1]))

#you can run the queue, it'll run
mainQueue()
