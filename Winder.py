#!/usr/bin/python
# File: Winder.py
# Description: Class for handling stepper motor operations.

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor

class Winder(object):

    # Constants for this stepper motor. These might need to be moved later.
    motor_port = 1              # Port that stepper motor is connected to.
    steps_per_rev = 200         # Number of steps/revolution for stepper motor.
    over_turn = 0.10            # Amount of overturn per revolution.
    turns_between_pause = 5     # Number of turns before pause and/or reverse direction.

    def __init__(self, turns_per_day, rpm, turn_type):
        self.turns_per_day = turns_per_day
        self.rpm = rpm
        self.turn_type = turn_type
        self.rot_count = 0
        self.pause_interval()
        self.steps_per_turn()

    def turn_off_motors(self):
        self.motor_hat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.motor_hat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.motor_hat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.motor_hat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    def create_motor_hat(self):
        self.motor_hat = Adafruit_MotorHAT()

    def create_stepper(self):
        self.my_stepper = self.motor_hat.getStepper(self.steps_per_rev, self.motor_port)
        self.my_stepper.setSpeed(self.rpm)

    def pause_interval(self):
        self.pause = (60 * 60 * 24) / (self.turns_per_day / self.turns_between_pause)

    def steps_per_turn(self):
        self.total_steps = int(self.steps_per_rev * (1 + self.over_turn))

    def rotate_watch(self):
        self.create_motor_hat()
        self.create_stepper()
        i = 0
        while(i < self.turns_between_pause):
            if (self.turn_type == "CW"):
                self.my_stepper.step(self.total_steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
            elif (self.turn_type == "CCW"):
                self.my_stepper.step(self.total_steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
            elif (self.turn_type == "ALT" and self.rot_count % 2 == 0):
                self.my_stepper.step(self.total_steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
            elif (self.turn_type == "ALT" and self.rot_count % 2 == 1):
                self.my_stepper.step(self.total_steps, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
            else:
                print("Bad config.")
            self.rot_count = self.rot_count + 1
            i = i + 1
        self.turn_off_motors()

    # Needed so that motor hat can be killed outside of class.
    def get_motor_hat(self):
        return self.motor_hat

    def get_turn_count(self):
        return self.rot_count

    def get_pause_interval(self):
        return self.pause
