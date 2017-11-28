#!/usr/bin/python
# File: Winder.py
# Description: Class for handling stepper motor operations.

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor

class Winder(object):

    # Constants for this stepper motor. These might need to be moved later.
    motor_port = 1          # Port that stepper motor is connected to.
    steps_per_rev = 200     # Number of steps/revolution for stepper motor.
    turns_between_pause = 5  # Number of turns before pause and/or reverse direction.

    def __init__(self, turns_per_day, rpm, turn_type):
        self.turns_per_day = turns_per_day
        self.rpm = rpm
        self.turn_type = turn_type
        self.rot_count = 0
        pause_interval(self):

    def turn_off_motors(self):
        motor_hat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        motor_hat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        motor_hat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        motor_hat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    def create_motor_hat(self):
        self.motor_hat = Adafruit_MotorHAT()

    def create_stepper(self):
        self.my_stepper = stepper_motor.getStepper(self.steps_per_rev, self.motor_port)
        self.my_stepper.setSpeed(self.rot_rate)

    def pause_interval(self):
        self.pause = (60 * 60 * 24) / (rotations_per_day / rots_between_pause)

    def rotate_watch(self):
        create_motor_hat(self)
        create_stepper(self)
        i = 0
        while(i < turns_between_pause):
            if (rotation_type == "CW"):
                stepper.step(steps_per_rev, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
            elif (rotation_type == "CCW"):
                stepper.step(steps_per_rev, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
            elif (rotation_type == "ALT" and global_count % 2 == 0):
                stepper.step(steps_per_rev, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
            elif (rotation_type == "ALT" and global_count % 2 == 1):
                stepper.step(steps_per_rev, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
            else:
                print("Bad config.")
            rot_count = rot_count + 1
            i = i + 1
        turn_off_motors(self)

    # Needed so that motor hat can be killed outside of class.
    def get_motor_hat():
        return motor_hat

    def get_turn_count():
        return rot_count

    def get_pause_interval():
        return pause
