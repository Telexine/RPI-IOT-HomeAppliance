#!/usr/bin/env python3

import RPi.GPIO as GPIO
import datetime as t
from time import sleep
from firebase import firebase

GPIO.setmode(GPIO.BCM)

#INIT
devicesID = {
    's1' :{'pin': 17},
    's2' :{'pin': 18},
    's3' :{'pin': 27},
    's4' :{'pin': 22},
    's5' :{'pin': 23},
    's6' :{'pin': 24},
    's7' :{'pin': 10},
    's8' :{'pin': 9}
}

for i in devicesID:
    GPIO.setup(devicesID[i]['pin'], GPIO.OUT)
#END INIT

def compareState(devices,getState):
    if GPIO.input(devicesID[devices]['pin']) == getState:
	
        if getState == True:
            GPIO.output(devicesID[devices]['pin'], GPIO.LOW)
	    print "%s : DEVICE   %s   Turn ON "  % (t.datetime.now(),devices)
        else:
            GPIO.output(devicesID[devices]['pin'], GPIO.HIGH)
	    print "%s : DEVICE   %s   Turn OF "  % (t.datetime.now(),devices)


firebase = firebase.FirebaseApplication('https://rpi-iot-homeappliance.firebaseio.com', None)
while True:
    
        s1 = firebase.get('/devicesID','1/state')
        s2 = firebase.get('/devicesID','2/state')
        s3 = firebase.get('/devicesID','3/state')
        
        compareState('s1',s1)
        compareState('s2',s2)
        compareState('s3',s3)

        sleep(0.01)


GPIO.cleanup()
