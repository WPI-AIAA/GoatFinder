import time
import GPIO
import datetime

//Hall effects are 23 and 24

GPIO.setup(23 , GPIO.IN)

GPIO.add_event_detect(17, GPIO.BOTH, callback=sensorCallback1)

def sensorCallback1(channel):
  # Called if sensor output goes LOW
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  print("Sensor LOW " + stamp)
