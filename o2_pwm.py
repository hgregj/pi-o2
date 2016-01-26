#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time, os

# Initialise the PWM device using the default address
pwm = PWM(0x40)

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

def led_on(channel):
  pwm.setPWM(channel,0,0)


def led_off(channel):
  pwm.setPWM(channel,4096,2000)


  # and now servo on Channel 1
def servo_press(channel, servoMin, servoMax):
    if (servoMin < servoMax) :
        step = 25
    else:
        step = -25
        
    for angle in range(servoMin,servoMax, step):
        time.sleep(0.01)
        pwm.setPWM(channel, 0, angle)

    for angle in range(servoMax,servoMin, 0-step):
        time.sleep(0.01)
        pwm.setPWM(channel, 0, angle)
    
