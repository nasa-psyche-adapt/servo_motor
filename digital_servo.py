import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin D5.
pwm = pwmio.PWMOut(board.D5, duty_cycle=2 ** 15,  frequency=50)    #gpio/bcm number (not board number)

# Create a servo object.
servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        servo.angle = angle
        time.sleep(0.05)

# SOURCE: https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/pwm-outputs-servos
# OLD FILE NAME: PWM_motor_servo_control.py
