Task 1: The inertial Measurement Unit (MU)  
If you dont add clear all the port will not clear, so can't reconnect to com3 port as it believes there is already a connection  
  
The incoming serial data uses a buffer to store data that the program might not be able to process yet,  
but if you restart the program, some of the previous data is still in the buffer. So on start there might be some random data as a start point.  
Instead restarting matlab fully clears the buffer and gets rid of this problem  

![image](https://github.com/user-attachments/assets/bdbf100c-8b46-41d0-9539-5a2825e4acc4)  
  
![image](https://github.com/user-attachments/assets/64514818-4125-49dd-8c8d-c8d466dcc8c1)  
Holding the pybench flat and horizontally (long side facing you):  
Blue is pitch (Up and down)
tilting Away from you blue goes down (angle increases), towards you it goes up (angle decreases)  
Outputs angle as a radian
Red is roll (left and right)  
tilting Left makes red go up, right makes red go down   
This is due to it measuring the effect of gravity on the displacement of the weight / springs near to the 2 capacitor plates  

  
Shaking it gives the same effect as tilting because the it responds to any acceleration  
Also Slight motion of the accelerometer adds 'noise' to the reading  
![image](https://github.com/user-attachments/assets/bc25fc3b-5d82-4d63-98fe-e421fc575e7b)

Gyroscope:  
We use it to read angular velocity
Gives an estimate of the angle split into pitch and roll:
![image](https://github.com/user-attachments/assets/83df9bf0-363d-40d0-a4c0-776962b28962)

take pdot (ang velocity) and multiply it by delta t (time change) and add that to the previous angle's reading :
![image](https://github.com/user-attachments/assets/bde77411-edda-4d88-be4d-7cfaed6bd7df)
Measuring velocity instead of accelleration removes the noise due to force.   
Toc gives the elapsed time since the last tic.  
gx is the estimated roll angle, tben we use the formula to iteratively update it. 
Max(min(,-pi/2)+pi/2) is used to restrict the display to +- pi/2  
Shaking it does not change the reading as the angle is based on velocity instead of acceleration.

However, the gyro reading goes up linearly when there is an initial offset.   
If the first reading is not 0, this error gets added every time in the inegration.  


Task 2: 3D plot  
When you shake the acceleration moves but not gyroscope.  
Gyroscope drifts due to the integration producing a 'dc offset'   
Accellerometer is moves more, but gyroscope is much more accurate  

Task 3: Complementary filter  

Low pass on accel to remove 'noise'  
'noise' Acts similar to high freq sound noise  
high pass on accel to remove 'dc offset'  
This is a low freq because it changes slowly  
Add them together to get the best reading for all freq.  
![image](https://github.com/user-attachments/assets/ea00bef7-ea73-4f46-98de-eb6e0e726c85)

Task 4:  
When all 3 pybench switches are set to 000, when the pybench turns on and runs main.py,  
The 000 causes it to run user.py, and you can put in user.py execfile("myprog.py") to run myprog.py.
Just need to drop it into the SD card disk.  
It runs the program in a loop   
????  
mac terminal allows for control c / d interaction   
![image](https://github.com/user-attachments/assets/e418ea10-2891-4810-ae56-425b5c69d383)  
Second I2C on oled is used   
i2c.scan() finds the i2c address  
the OLED is created with 6 different pins such as reset pin  
The device id is also added.  

  
![image](https://github.com/user-attachments/assets/65838011-ecb3-4320-bdcb-9a80d2b05a92)

30, 30 spacing centres 'Hello World!'  

Task 4 extra:  
Using Oled.Line instead as angle changes work better
Had to find pot.read() in python test code.  

Task 5:

Correctly Shifts when tilted
