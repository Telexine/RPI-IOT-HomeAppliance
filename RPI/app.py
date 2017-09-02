#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep
from firebase import firebase
import json

firebase = firebase.FirebaseApplication('https://rpi-iot-homeappliance.firebaseio.com', None)
controls = firebase.get('/devicesID', None)
while True:

	s1 = firebase.get('/devicesID','1/state')
	s2 = firebase.get('/deviceID','2/state')
	s3 = firebase.get('/deviceID','3/state')

	sleep(2)
