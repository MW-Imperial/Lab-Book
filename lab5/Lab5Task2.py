import pyb
from pyb import Pin, ADC, Timer
from oled_938 import OLED_938  # Use OLED display driver

# Create peripheral objects
b_LED = LED(4)        # Blue LED
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

A_sense = Pin("Y6", Pin.PULL_NONE)
B_sense = Pin("Y4", Pin.PULL_NONE)

A_state = 0
A_speed = 0
A_count = 0
tic = pyb.millis();

tim = Timer(2, freq=1000)
motorA = tim.channel (1, Timer.PWM, pin = PWMA)
motorB = tim.channel (2, Timer.PWM, pin = PWMB)

def A_forward(value):
    A1.low()
    A2.high()
    motorA.pulse_width_percent(value)

def B_forward(value):
    B1.low()
    B2.high()
    motorB.pulse_width_percent(value)

while True:
    if (A_state == 0) and (A_sense.value()==1):
        A_count += 1
        print("count")
    A_state = A_sense.value()
    print(A_sense.value())
    toc = pyb.millis()
    if ((toc-tic) >= 1000):
        A_speed = A_count
        tic = pyb.millis()
        A_count = 0
        print(A_speed)
        value = pot.read()
        mapped = ((value) * (100) / (4095))
        A_forward(mapped)
        B_forward(mapped)
        oled.clear()
        oled.draw_text(60,20, '{:5.2f} rps'.format(A_speed/39))
        potangle =  (value) * (180) / (4095 ) + -90
        oled.line(96, 26, potangle, 24, 1)
        oled.display()
