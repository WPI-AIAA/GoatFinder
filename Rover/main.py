
from enum import Enum
import threading
from thread_objects import *
import nav_loader 
from time import sleep
import drive as dr
#from navSystem_hall import navsystem

class State(Enum):
	TEST = 1
	STANDBY = 2
	ARM = 3

# Initialization
# Run setup and tests

hall_reader = threading.Thread(target = hall_thread, daemon = True)
nine_dof_reader = threading.Thread(target = nine_dof_thread, daemon = True)

global nav_loader
nav_loader.init()


# Go Into Operation Mode
hall_reader.start()
nine_dof_reader.start()


#Nathan's really old stuff (w/ two example functions)
from PIDcontrol import PID
from functionQueue import *

#testing PID
#controller = PID(1,1,1,.5)

sleep(5)

import motorOutput as mot

#while True:
#        for i in range (0,11):
#                mot.driveleftmotor(i/10)
#                mot.driverightmotor(i/10)
#                nav_loader.nav.read_displacement()
#                sleep(1)

import cameraHelper as camH
import servos
import altitudedetection as altd
'''
addToQueue([altd.initializealt])
addToQueue([altd.ismovingup])
addToQueue([altd.ismovingdown])
addToQueue([altd.isstationary])
addToQueue([servos.releaseparachute])
addToQueue([dr.turn, 0])
addToQueue([camH.takepic1])
addToQueue([dr.turn, 1.5])
addToQueue([camH.takepic2])
addToQueue([dr.turn, 3.1])
addToQueue([camH.takepic3])
addToQueue([dr.turn, -1.5])
addToQueue([camH.takepic4])
addToQueue([dr.turn, 0])
addToQueue([servos.dropfirst])
addToQueue([dr.drive, [120,0],[0,0]])
addToQueue([servos.dropsecond])
addToQueue([dr.drive, [120,120],[120,0])
addToQueue([mot.stopmotors])
'''

#you can add functions to the queue
addToQueue((dr.drive, [10, 0],[0,0]))
addToQueue((dr.drive, [10,10],[10,0]))

print("about to start queue")
sleep(5) # get some accelerometer data to avoid NaNs

#you can run the queue, it'll run
mainQueue()
