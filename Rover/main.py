
from enum import Enum
import threading
from thread_objects import *

class State(Enum):
	TEST = 1
	STANDBY = 2
	ARM = 3

# Initialization
# Run setup and tests

hall_reader = threading.Thread(target = hall_thread, daemon = True)
nine_dof_reader = threading.Thread(target = nine_dof_thread, daemon = True)


# Go Into Operation Mode
hall_reader.run()
nine_dof_reader.run()


#Nathan's really old stuff (w/ two example functions)
from PIDcontrol import PID
from functionQueue import *

def doAThing(arg1, arg2):
    print(arg1)
    print(arg2)
def doAnotherThing(arg1):
    print(arg1)

#testing PID
#controller = PID(1,1,1,.5)

#you can add functions to the queue
addToQueue((doAThing, "ASDASDJSAFKJHASFKHE", "asdfs"))
addToQueue((doAnotherThing, 3+4))

#you can run the queue, it'll run
mainQueue()
