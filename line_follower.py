from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

LIGHT_VALUE = 50
MAX_SPEED = 15
ROTATION_SPEED = 30

# Create your objects here.
hub = MSHub()

motor_pair = MotorPair('A', 'B')

left_sensor = ColorSensor('C')
right_sensor = ColorSensor('D')

motor_pair.set_default_speed(MAX_SPEED)

while True:
    left_light = left_sensor.get_reflected_light()
    right_light = right_sensor.get_reflected_light()
    if left_light > LIGHT_VALUE and right_light > LIGHT_VALUE:
        print(left_light, right_light, 'GERADEAUS!')
        motor_pair.start()
    elif left_light < LIGHT_VALUE:
        print(left_light, right_light, 'RECHTS!')
        motor_pair.move_tank(ROTATION_SPEED, 'degrees', MAX_SPEED, -MAX_SPEED)
    elif right_light < LIGHT_VALUE:
        print(left_light, right_light, 'RECHTS!')
        motor_pair.move_tank(ROTATION_SPEED, 'degrees', -MAX_SPEED, MAX_SPEED)
