
# ----------------------------------------------------------------
# Name: Lab 4 Task 5 – display pitch angle on OLED
# ----------------------------------------------------------------
# Creator:    Peter YK Cheung
# Date:       5 Feb 2022
# Revision:   2
# ----------------------------------------------------------------
# Put comments here to explain what this does
# ----------------------------------------------------------------

import pyb
from pyb import LED
from oled_938 import OLED_938
from mpu6050 import MPU6050
from pyb import Pin, Timer


# Define LEDs
b_LED = LED(4)

# I2C connected to Y9, Y10 (I2C bus 2) and Y11 is reset low active
i2c = pyb.I2C(2, pyb.I2C.MASTER)
devid = i2c.scan()  # Find the I2C device number
oled = OLED_938(
    pinout={"sda": "Y10", "scl": "Y9", "res": "Y8"},
    height=64, external_vcc=False, i2c_devid=i2c.scan()[0]
)

oled.poweron()
oled.init_display()

# IMU connected to Y9 and X10
imu = MPU6050(1, False)  # Use I2C port 1 on Pyboard

def read_imu(dt):
    global g_pitch
    global g_roll
    alpha = 0.7  # Larger = longer time constant
    pitch = int(imu.pitch())
    roll = int(imu.roll())
    g_pitch = alpha * (g_pitch + imu.get_gy()*dt*0.001) + (1-alpha)*pitch
    g_roll = alpha * (g_roll + imu.get_gy()*dt*0.001) + (1-alpha)*roll

g_pitch = 0
tic = pyb.millis()

# Create peripheral objects
b_LED = LED(4)        # Blue LED

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

tim = Timer(2, freq=1000)
motorA = tim.channel (1, Timer.PWM, pin = PWMA)
motorB = tim.channel (2, Timer.PWM, pin = PWMB)

A_sense = Pin("Y6", Pin.PULL_NONE)
B_sense = Pin("Y4", Pin.PULL_NONE)

A_state = 0
A_speed = 0
A_count = 0

B_state = 0
B_speed = 0
B_count = 0

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

g_roll = 0
g_pitch = 0

tic = pyb.millis()
tic2 = pyb.millis()


while True:
    if (A_state == 0) and (A_sense.value()==1):
        A_count += 1
        print("count")
    A_state = A_sense.value()
    print(A_sense.value())
    
    if (B_state == 0) and (B_sense.value()==1):
        B_count += 1
        print("count")
    B_state = B_sense.value()
    print(B_sense.value())
    toc = pyb.millis()

    if ((toc-tic2) >= 1000):

        A_speed = A_count 
        B_speed = B_count  
        A_count = 0
        B_count = 0
        tic2 = pyb.millis()

    read_imu(tic-toc)

    mapped_pitch = ((g_pitch/180)*100)
    mapped_roll = ((g_roll/180)*100)
    print(g_pitch)
    print(g_roll)
    if (mapped_roll > 0):
        A_forward(mapped_roll)  
        
    else:
        A_back(abs(mapped_roll))

        
    if (mapped_pitch > 0):

        B_forward(mapped_pitch) 
    else:

        B_back(abs(mapped_pitch))
        
    oled.clear() 
    oled.draw_text(60, 20, '{:5.2f} rps'.format(A_speed / 19))  
    oled.draw_text(10, 20, '{:5.2f} rps'.format(B_speed / 19)) 
    oled.display()
    tic = pyb.millis()
 
