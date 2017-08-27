 

import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
 
 
pins = {

   17 : {'name' : 'GrapOpen     (17)', 'state' : GPIO.LOW},
   18 : {'name' : 'GrapClose    (18)', 'state' : GPIO.LOW},
   27 : {'name' : 'AnkleOpen    (27)', 'state' : GPIO.LOW},
   22 : {'name' : 'AnkleClose   (22)', 'state' : GPIO.LOW},
   23 : {'name' : 'BaseCW       (23)', 'state' : GPIO.LOW},
   24 : {'name' : 'BaseCCW      (24)', 'state' : GPIO.LOW},
   10 : {'name' : 'AnkleCW      (10)', 'state' : GPIO.LOW},
   9 :  {'name' : 'AnkleCCW     (09)', 'state' : GPIO.LOW}

   }

joints = {

    'Grap'  : {'0' : 17, '1': 18, 'state' : "idle"},
    'Ankle' : {'0' : 27, '1': 22, 'state' : "idle"},
    'Base'  : {'0' : 23, '1': 24, 'state' : "idle"},
    'Ankle_Turn'  : {'0' : 10, '1': 9, 'state' : "idle"},
   }
 


for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.HIGH)

for joint in joints:
     
    GPIO.setup(joints[joint]['0'], GPIO.OUT)
    GPIO.setup(joints[joint]['1'], GPIO.OUT)

    GPIO.output(joints[joint]['0'], GPIO.HIGH)
    GPIO.output(joints[joint]['1'], GPIO.HIGH)

@app.route("/")
def main():
    
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
    
   templateData = {
      'pins' : pins
      }
   
   return render_template('main.html', **templateData)

 
@app.route("/manual/<changePin>/<action>")
def m_action(changePin, action):
    
   changePin = int(changePin)
   
   deviceName = pins[changePin]['name']
    
   if action == "on":
      GPIO.output(changePin, GPIO.HIGH)
      message = "Turned " + deviceName + " off"
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " on."

   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

@app.route("/<Joint>/<logic>")
def action(Joint, logic):
    
   deviceLogic0 = int(joints[Joint]['0'])
   deviceLogic1 = int(joints[Joint]['1'])

   if logic == "0":
        GPIO.output(deviceLogic0, GPIO.LOW)
        GPIO.output(deviceLogic1, GPIO.HIGH)
   elif logic == "1":
        GPIO.output(deviceLogic1, GPIO.LOW)
        GPIO.output(deviceLogic0, GPIO.HIGH)
   else:
       GPIO.output(deviceLogic0, GPIO.HIGH)
       GPIO.output(deviceLogic1, GPIO.HIGH)

   for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)
        
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)