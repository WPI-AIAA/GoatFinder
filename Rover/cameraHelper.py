import picamera

camera = picamera.PiCamera()

def takepic1():
    camera.capture('/var/www/html/image1.jpg')
    
def takepic2():
    camera.capture('/var/www/html/image2.jpg')
    
def takepic3():
    camera.capture('/var/www/html/image3.jpg')
    
def takepic4():
    camera.capture('/var/www/html/image4.jpg')
