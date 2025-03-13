import pyb
from pyb import Pin, ADC, Timer
from oled_938 import OLED_938  # Use OLED display driver
import micropython
from pyb import ExtInt
micropython.alloc_emergency_exception_buf(100)

# Create peripheral objects
pyb.LED = LED(4)        # Blue LED
pot = ADC(Pin('X11')) # 5k ohm potentiometer to ADC input on pin X11

# I2C connected to Y9 (SDA), Y10 (SCL) pins and Y11 is reset (low active)
i2c = pyb.I2C(2, pyb.I2C.MASTER)  # Create I2C bus
dev_id = i2c.scan()               # Find the I2C device number
oled = OLED_938(
    pinout={"sda": "Y10", "scl": "Y9", "res": "Y8"},
    height=64,
    external_vcc=False,
    i2c_devid=i2c.scan()[0]
)



oled.poweron()
oled.init_display()

A1 = Pin("X4", Pin.OUT_PP)
A2 = Pin("X3", Pin.OUT_PP)

B1 = Pin("X8", Pin.OUT_PP)
B2 = Pin("X7", Pin.OUT_PP)

PWMA = Pin("X1")
PWMB = Pin("X2")


tim = Timer(2, freq = 1000)
motorA = tim.channel (1, Timer.PWM, pin = PWMA)
motorB = tim.channel (2, Timer.PWM, pin = PWMB)  

A_sense = Pin("Y6", Pin.PULL_NONE)
B_sense = Pin("Y4", Pin.PULL_NONE)

def A_forward(value):
    A1.low()
    A2.high()
    motorA.pulse_width_percent(value)

def B_forward(value):
    B1.low()
    B2.high()
    motorB.pulse_width_percent(value)

def A_back(value):
    A2.low()
    A1.high()
    motorA.pulse_width_percent(value)

def B_back(value):
    B2.low()
    B1.high()
    motorB.pulse_width_percent(value)

def A_stop(value):
    A1.high()
    A2.high()

def B_stop(value):
    B1.high()
    B2.high()

A_speed = 0
A_count = 0
B_speed = 0
B_count = 0


def isrA_motor(dummy):
    global A_count
    A_count += 1
    print(A_count)

def isrB_motor(dummy):
    global B_count
    B_count += 1

def isr_speed_timer(dummy):
    global A_count
    global A_speed
    global B_count
    global B_speed
    A_speed = A_count
    B_speed = B_count
    A_count = 0
    B_count = 0
    print(A_speed)

motorA_int = ExtInt ('Y6', ExtInt.IRQ_RISING, Pin.PULL_NONE, isrA_motor)
motorB_int = ExtInt ('Y4', ExtInt.IRQ_RISING, Pin.PULL_NONE, isrB_motor)

speed_timer =  pyb.Timer(4, freq=50)
speed_timer.callback(isr_speed_timer)


while True:
    value = pot.read()
    mapped = ((value-2048)*200/4096)
    if (mapped > 0):
        A_forward(mapped)  
        B_forward(mapped) 
    else:
        A_back(abs(mapped))
        B_back(abs(mapped))
        
    oled.clear() 
    oled.draw_text(60, 20, '{:5.2f} rps'.format(A_speed / 39))  
    potangle = (value * 180) / 4095 - 90  
    oled.line(96, 26, potangle, 24, 1)
    oled.display()
    pyb.delay(100)  
