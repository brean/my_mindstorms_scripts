from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()

motor_gripper = Motor('E')

def open_gripper():
    motor_gripper.run_to_position(0, 'clockwise', 50)
    
def close_gripper():
    motor_gripper.run_to_position(177, 'counterclockwise', 50)
    
open_gripper()
close_gripper()
