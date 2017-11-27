#!/usr/bin/python

import time, atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

# Stepper configuration TODO: Move into configuration file.
motor_port = 1
steps_per_rev = 200
rotation_rate = 15
rotations_between_pause = 5
rotation_type = "ALT" # CW = clockwise, CCW = counterclockwise, ALT = alternate direction
rotations_per_day = 750


def turn_off_motors(motor_hat):
    motor_hat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    motor_hat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    motor_hat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    motor_hat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

def sleep_between_rotations(rotations_per_day, rotations_between_pause, rotation_rate):
    # TODO: Calculate sleep time.
    return 30

def configure_stepper():
    motor_hat = Adafruit_MotorHAT()
    atexit.register(turn_off_motor(motor_hat))
    my_stepper = stepper_motor.getStepper(steps_per_rev, motor_port)
    my_stepper.setSpeed(rotation_rate) # RPM
    return my_stepper

def main():
    stepper = configure_stepper()
    global_count = 0
    while (global_count < rotations_per_day):
        if (rotation_type == "CW"):
            stepper.step(steps_per_rev, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.INTERLEAVE)
        elif (rotation_type == "CCW"):
            stepper.step(steps_per_rev, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.INTERLEAVE)
        elif (rotation_type == ALT && global_count % 2 == 0):
            stepper.step(steps_per_rev, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.INTERLEAVE)
        elif (rotation_type == ALT && global_count % 2 == 1):
            stepper.step(steps_per_rev, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.INTERLEAVE)
        else:
            print ("Bad configuration.")
            exit(1)
        global_count = global_count + 1
        sleep(sleep_between_rotations(rotations_per_day, rotations_between_pause, rotation_rate))
            
main()
