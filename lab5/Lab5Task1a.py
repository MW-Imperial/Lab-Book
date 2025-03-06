import pyb
from pyb import Pin, Timer

A1 = Pin("X4", Pin.OUT_PP)
A2 = Pin("X3", Pin.OUT_PP)

B1 = Pin("X7", Pin.OUT_PP)
B2 = Pin("X8", Pin.OUT_PP)

PWMA = Pin("X1")
PWMB = Pin("X2")

tim = Timer(2, freq=1000)
motorA = tim.channel(1, Timer.PWM, pin = PWMA)
motorB = tim.channel(2, Timer.PWM, pin = PWMB)

def motorA_Forward(value)
    A1.low()
    A2.high()
    motorA.pulse_width_percent(value)

def motorB_Forward(value)
    B1.low()
    B2.high()
    motorB.pulse_width_percent(value)

def motorA_Backward(value)
    A2.low()
    A1.high()
    motorA.pulse_width_percent(value)

def motorB_Backward(value)
    B2.low()
    B1.high()
    motorB.pulse_width_percent(value)

def motorA_stop(value)
    A1.low()
    A2.low()
    motorB.pulse_width_percent(value)

def motorB_stop(value)
    B1.low()
    B2.low()
    motorB.pulse_width_percent(value)