import pyb
from pyb import Pin, Timer

A1 = Pin("X4", Pin.OUT_PP)
A2 = Pin("X3", Pin.OUT_PP)

PWMA = Pin("X1")

tim = Timer(2, freq=1000)
motorA = tim.channel (1, Timer.PWM, pin = PWMA)

def A_Forward(value)
    A1.low()
    A2.high()
    motorA.pulse_width_percent(value)

pot = pyb.ADC(Pin('X11'))
value = pot.read()
mapped = ((value) * (50) / (4096))

A_Forward(mapped)