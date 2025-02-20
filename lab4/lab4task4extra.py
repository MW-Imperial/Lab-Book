# ----------------------------------------------------------------
# Name: Lab 4 Task 4
# ----------------------------------------------------------------
# Learning to use the OLED display driver
#
# Creator:    Peter YK Cheung
# Date:       9 Feb 2021
# Revision:   1.1
# ----------------------------------------------------------------

# Import pyboard basic library
import pyb
from pyb import LED, ADC, Pin  # Use various class libraries in pyb
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

# Simple Hello World message


t0 = pyb.millis()  # Store start time

while True:
    oled.clear()
    b_LED.toggle()
    toc = pyb.millis() - t0  # Read elapsed time
    oled.display()
    t0 = pyb.millis()  # Start time
    potval = pot.read()
    potangle =  (potval) * (180) / (4095 ) + -90
    oled.line(96, 26, potangle, 24, 1)
    oled.display()
    delay = pyb.rng() % 1000  # Generate random number between 0 and 999

    pyb.delay(delay)  # Delay in milliseconds

