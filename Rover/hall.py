import time
import GPIO
import datetime


//These pins are not the correct pins
GPIO.setup(17 , GPIO.IN)

GPIO.add_event_detect(17, GPIO.BOTH, callback=sensorCallback1)

def sensorCallback1(channel):
  # Called if sensor output goes LOW
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  print("Sensor LOW " + stamp)
