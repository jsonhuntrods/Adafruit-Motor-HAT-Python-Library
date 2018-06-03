#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor
import time
import atexit
import threading
import random

bottomhat = Adafruit_MotorHAT(addr=0x61)
tophat = Adafruit_MotorHAT(addr=0x60)

stepperThreads = [threading.Thread(), threading.Thread(), threading.Thread()]

def turnOffMotors():
    tophat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    tophat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    tophat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    tophat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    bottomhat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    bottomhat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    bottomhat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    bottomhat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper1 = bottomhat.getStepper(200, 2)
myStepper2 = tophat.getStepper(200, 1)
myStepper3 = tophat.getStepper(200, 2)

myStepper1.setSpeed(60)
myStepper2.setSpeed(60)
myStepper3.setSpeed(60)

steppers = [myStepper1, myStepper2, myStepper3]

def stepper_worker(stepper, numsteps, direction, style):
    #print("Steppin!")
    stepper.step(numsteps, direction, style)
    #print("Done")

for i in range(3):
    if not stepperThreads[i].isAlive():
        stepperThreads[i] = threading.Thread(target=stepper_worker, args=(steppers[i], 200, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE))
        stepperThreads[i].start()
