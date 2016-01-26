from flask import render_template
from app import app
from Adafruit_PWM_Servo_Driver import PWM
import os, time
import datetime

from  o2_pwm import led_on, led_off, servo_press

# Initialise the PWM device using the default address
pwm = PWM(0x40)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
conentratorOn = False


@app.route('/')
@app.route('/index')
def index():
    led_on(4)
    os.system("raspistill -n -t 2000 -md 6 -q 9 -br 50 --roi .2,.2,.8,.8 -o /home/pi/O2-control/app/static/pic2.jpg")
    led_off(4)

    print "Status is:OFF at:", datetime.datetime.now()
    dateString = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    user = {'nickname': 'greg'}  # fake user
    status = { 'iconFile' : '/static/OFF_icon.jpg',
               'message' : 'Concentrator is off' }
    status['dateTime'] = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    print "Status dictionary::", status 
	
    return render_template("index.html",
                           title='Concentrator',
                           user=user,
                           status=status)



@app.route('/toggle')
def o2Toggle():
    if concentratorOn:
	o2Stop()
    else:
	o2Start()




@app.route('/start')
def o2Start():
    
    led_on(4)
    servo_press(1,servoMin,servoMax)
    os.system("raspistill -n -t 2000 -md 6 -q 9 -br 50 --roi .2,.2,.8,.8 -o /home/pi/O2-control/app/static/pic2.jpg")
    led_off(4)
    concentratorOn = True

    print "Status is:ON at:", datetime.datetime.now()
    dateString = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    user = {'nickname': 'greg'}  # fake user
    status = { 'iconFile' : '/static/ON_icon.jpg',
               'message' : 'Concentrator is starting' }
    status['dateTime'] = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    print "Status dictionary::", status 
	
    return render_template("index.html",
                           title='Concentrator',
                           user=user,
                           status=status)

@app.route('/stop')
def o2Stop():
    
    led_on(4)
    servo_press(0,servoMax,servoMin)
    os.system("raspistill -n -t 2000 -md 6 -q 9 -br 50 --roi .2,.2,.8,.8 -o /home/pi/O2-control/app/static/pic2.jpg")
    led_off(4)
    concentratorOn = False

    print "Status is:OFF at:", datetime.datetime.now()
    dateString = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    user = {'nickname': 'greg'}  # fake user
    status = { 'iconFile' : '/static/OFF_icon.jpg',
               'message' : 'Concentrator is stopping' }
    status['dateTime'] = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    print "Status dictionary::", status 
	
    return render_template("index.html",
                           title='Concentrator',
                           user=user,
                           status=status)






