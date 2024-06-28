from adafruit_servokit import ServoKit
import time

def OpenDoor(angle):
    time.sleep(1)
    kit = ServoKit(channels=16)
    kit.servo[0].angle = 90
    kit.continuous_servo[1].throttle = 1
    time.sleep(1)
    kit.continuous_servo[1].throttle = -1
    time.sleep(1)
    kit.servo[0].angle = 0
    kit.continuous_servo[1].throttle = 0