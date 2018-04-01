
from enum import Enum

class State(Enum):
	TEST = 1
	STANDBY = 2
	ARM = 3

# Initialization
# Run setup and tests



# Go Into Operation Mode


#Nathan's really old stuff (w/ two example functions)
from PIDcontrol import PID
from functionQueue import *

def doAThing(arg1, arg2):
    print(arg1)
    print(arg2)
def doAnotherThing(arg1):
    print(arg1)

if __name__ == '__main__':
    #testing PID
    #controller = PID(1,1,1,.5)

    #you can add functions to the queue
    addToQueue((doAThing, "ASDASDJSAFKJHASFKHE", "asdfs"))
    addToQueue((doAnotherThing, 3+4))

    #you can run the queue, it'll run
    mainQueue()
