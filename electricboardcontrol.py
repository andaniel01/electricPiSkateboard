import os     
import time   
time.sleep(1)
import pigpio
from evdev import InputDevice, categorize, ecodes

ESC=13   

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0) 

max_value = 4000
min_value = 700

gamepad = InputDevice('/dev/input/event7')

up = 544
down = 545
right = 547
left = 546
oBtn = 305


def drive():
    print ("you're in drive now")
    speed = 1500
    
    for event in gamepad.read_loop():
         if event.type == ecodes.EV_KEY:
             if event.value == 1:
                 pi.set_servo_pulsewidth(ESC, speed)
                 if event.code == up:
                     print("go fast")
                     if speed != 2300:
                         speed = speed + 100
                     print("speed is {}".format(speed))
                 elif event.code == down:
                     print("go slow down fast")
                     speed = speed - 100
                     print("speed is ",speed)
                 elif event.code == right:
                     print("go slow")
                     if speed != 2300:
                         speed = speed + 10
                     print("speed is ",speed)
                 elif event.code == left:
                     print("go slow down slow")
                     speed = speed - 10
                     print("speed is ",speed)
                 elif event.code == oBtn:
                    pi.set_servo_pulsewidth(ESC, 0)
                    pi.stop()
drive()
            
            