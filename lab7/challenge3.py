# Import relevant packages that you use ...
import pyb
from pyb import Pin, Timer, ADC, DAC, LED
from oled_938 import OLED_938
from mpu6050 import MPU6050
import micropython  # Needed for interrupt


micropython.alloc_emergency_exception_buf(100)

# Initialise various peripherals e.g. OLED, IMU etc
pot = ADC(Pin('X11'))

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

# Initialise different constants, variables, arrays etc
alpha = 0.97
target_pitch = 0.5
error_sum = 0
pitch = 0

A1 = Pin("X4", Pin.OUT_PP)
A2 = Pin("X3", Pin.OUT_PP)

B1 = Pin("X8", Pin.OUT_PP)
B2 = Pin("X7", Pin.OUT_PP)

PWMA = Pin("X1")
PWMB = Pin("X2")

tim = Timer(2, freq=1000)
motorA = tim.channel (1, Timer.PWM, pin = PWMA)
motorB = tim.channel (2, Timer.PWM, pin = PWMB)

def A_forward(value):
    A1.low()
    A2.high()
    motorA.pulse_width_percent(value)

def B_forward(value):
    B1.high()
    B2.low()
    motorB.pulse_width_percent(value)

def A_back(value):
    A2.low()
    A1.high()
    motorA.pulse_width_percent(value)

def B_back(value):
    B2.high()
    B1.low()
    motorB.pulse_width_percent(value)

def A_stop(value):
    A1.high()
    A2.high()

def B_stop(value):
    B1.high()
    B2.high()

def pitch_estimate(dt, alpha):
    global pitch
    theta = int(imu.pitch())
    pitch_dot = imu.get_gy()
    pitch = alpha*(pitch + pitch_dot*(dt/1000000)) + (1-alpha) * theta
 
# Read the dancing steps from file into array

# Use Potentiometer and USR switch to tune Kp, Ki and Kd

trigger = pyb.Switch()
scale = 2

while not trigger():  # wait to tune Kp
    pyb.delay(1)
    K_p = 2.2#pot.read() * (scale*10) / 4095  # use pot to set Kp
    oled.draw_text(0, 30, 'Kp = {:5.2f}'.format(K_p))  # display live value on oled
    oled.display()

while trigger(): pass  # wait for button release

while not trigger():  # wait to tune Ki
    pyb.delay(1)
    K_i = 200#pot.read() * (scale*50) / 4095  # use pot to set Ki
    oled.draw_text(0, 40, 'Ki = {:5.2f}'.format(K_i))  # display live value on oled
    oled.display()

while trigger(): pass  # wait for button release

while not trigger():  # wait to tune Kd
    pyb.delay(1)
    K_d = 1#pot.read() * scale / 4095  # use pot to set Kd
    oled.draw_text(0, 50, 'Kd = {:5.2f}'.format(K_d))  # display live value on oled
    oled.display()

while trigger(): pass  # wait for button release

print('Button pressed. Running script.')
oled.draw_text(0, 20, 'Button pressed. Running.')
oled.display()

#Peter Bit

tic2 = pyb.millis()  # mark time now in msec

try:  # Try to handle exception
    tic1 = pyb.micros()
    while True:  # infinite loop
        dt = pyb.micros() - tic1  # loop period is 5 msec or 200Hz
        pitch_dot = imu.get_gy()
        pitch_estimate(dt, alpha)
        error = target_pitch - pitch
        print("error:", error)
        derivative = -pitch_dot
        error_sum = error*dt/1000000 +0.99*error_sum
        print("kp:", K_p)
        PID_Output = (K_p*error) + (K_i * error_sum) + (K_d * derivative)
        print("PID_Output:", PID_Output)
            
        PWM_in = max(15, min(abs(PID_Output), 100))
        print("pid_in", PWM_in)

            
            # use returned value to move motor
        if (PID_Output < 0):
            A_forward(PWM_in)
            B_forward(PWM_in)
            print("forward")
           

        elif PID_Output > 0:
            A_back(PWM_in)
            B_back(PWM_in)
            print("back")

        else:
            A_stop(0)
            B_stop(0)
                
            # if microphone buffer is full
            #     test if beat has occurred
            #     if yes, update the target of pitch angle
            #update tic1
        tic1 = pyb.micros()
        tic2 = pyb.millis()

finally:  # always executed if exception
    A_stop(0)
    B_stop(0)
