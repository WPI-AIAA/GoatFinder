# Goat Finder
### Worcester Polytechnic Institute AIAA
### Battle of the Rockets 2018



## Adding the Repository
Clone the repository to a directory
```
$~ git clone https://github.com/WPI-AIAA/GoatFinder
$~ git checkout dev
```

From here move into a specific branch
```
$~ git checkout <branch>
```

We will be working out of two primary branches within dev
```
groundStation
rover
```



## Setting up the PI Zero W


### Disable BlueTooth

1. Open config.txt
   `sudo nano /boot/config.txt`

2. Add the following line to the file
   `dtoverlay=pi3-disable-bt`

3. Reboot
   `sudo reboot`

### Enabling I2C 

Taken from [Adafruit](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)

1. Install I2C tools
   `sudo apt install -y python-smbus`
   `sudo apt install -y i2c-tools`

2. Install Kernel Support
   `sudo raspi-config`

3. Navigate to Interfacing Options and Enable I2C

4. Reboot
   `sudo reboot`

5. Check for attached I2C devices
   `sudo i2cdetect -y 1`

### Enable SPI

Taken from [Adafruit](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-spi)

1. ​Remove the blacklist for the SPI module
   `sudo nano /etc/modprobe.d/rapsi-blacklist.conf`

2. Reboot
   `sudo reboot`

3. Check the devices are available
   `ls -l /dev/spidev*`

### Enable UART

1. Install Serial Library
   `sudo apt install python-serial`

### Install Django

Taken from [Django](https://docs.djangoproject.com/)

1. Install Python
   `sudo apt install python3`

2. Setup a Database (optional)
   `place holder`

3. Install PIP
   `place holder`

4. Install Django
   `place holder`


## Standards

### General GPIO

We will be using the BCM GPIO numbering
```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
```

### Using I2C

I2C will be used to interface with the BMP280 and LSM9DS0
```python
import smbus
myDevice = smbus.SMBus(1) # The Pi has two available busses, 0 and 1
myAddress = 0x00 # Device address

def read(byte):
	return(myDevice.read_byte_data(myAddress, byte)) # Read a Byte

def write(byte, value):
	myDevice.write_byte_data(myAddress, byte, value) # Set a Byte to Value
```

### Using UART

UART will be used to interface with the XBEE Radio or GPS
```python
import serial
port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0) # ttyAMA0 corresponds to the UART interface

port.write("Sometext")
port.read(10) # Read 10 Characters
```

### XBEE

XBEE Radio Protocol Options
+ Ad Hoc Wireless Network Mode
+ Serial Communication Service
+ API Mode
