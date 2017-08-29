from flask import Flask, render_template, request
app = Flask(__name__)

#GPIO.setmode(GPIO.BCM)

# 8 Channel

#INIT STATE
pins = {
  ## PIN { ID,name, state (default off) }
   17 : {'id':'0','name' : 'Light 1     (17)', 'state' : GPIO.LOW},
   18 : {'id':'1','name' : 'Light 2     (18)', 'state' : GPIO.LOW},
   27 : {'id':'2','name' : 'Light 3     (27)', 'state' : GPIO.LOW},
   22 : {'id':'3','name' : 'Light 4     (22)', 'state' : GPIO.LOW},
   23 : {'id':'4','name' : 'Light 5     (23)', 'state' : GPIO.LOW},
   24 : {'id':'5','name' : 'Light 6     (24)', 'state' : GPIO.LOW},
   10 : {'id':'6','name' : 'Light 7     (10)', 'state' : GPIO.LOW},
   9 :  {'id':'7','name' : 'Light 8     (09)', 'state' : GPIO.LOW}

   }

joints = {
    'Grap'  : {'0' : 17, '1': 18, 'state' : "idle"},
    'Ankle' : {'0' : 27, '1': 22, 'state' : "idle"},
    'Base'  : {'0' : 23, '1': 24, 'state' : "idle"},
    'Ankle_Turn'  : {'0' : 10, '1': 9, 'state' : "idle"},
   }







@app.route("/")
def main():

#   for pin in pins:
#      pins[pin]['state'] = GPIO.input(pin)

   templateData = {
#      'pins' : pins
     }

   return render_template('main.html', **templateData)


@app.route("/control/<device_ID>/<action>")
def state_action(device_ID, action):

#   changePin = int(changePin)
 #  deviceName = pins[changePin]['name']


#STATE CHANGE
   templateData = {
  #    'pins' : pins
   }

   return render_template('main.html', **templateData)
