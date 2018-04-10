
from enum import Enum
import multiprocessing
from thread_objects import *
from nav_loader import nav

class State(Enum):
	TEST = 1
	STANDBY = 2
	ARM = 3

# Initialization
# Run setup and tests

hall_reader = multiprocessing.Process(target = hall_thread, daemon = True)
nine_dof_reader = multiprocessing.Process(target = nine_dof_thread, daemon = True)




# Go Into Operation Mode
hall_reader.start()
nine_dof_reader.start()


#Nathan's really old stuff (w/ two example functions)
from PIDcontrol import PID
from functionQueue import *
import drive as dr

#testing PID
#controller = PID(1,1,1,.5)

#you can add functions to the queue
addToQueue((dr.drive, [1,1],[0,0]))
addToQueue((dr.drive, [0,0],[1,1]))

print("about to start queue")

#you can run the queue, it'll run
mainQueue()
