# GoatFinder
### Worcester Polytechnic Institute AIAA
### Battle of the Rockets 2018



## Adding the Repository
Clone the repository to a directory
```
$~ git clone https://github.com/WPI-AIAA-BOR/GoatFinder
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

### General GPIO

We will be using the BCM GPIO numbering
```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
```