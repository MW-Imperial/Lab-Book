Task 1: The inertial Measurement Unit (MU)  
If you dont add clear all the port will not clear, so can't reconnect to com3 port as it believes there is already a connection  
The incoming serial data uses a buffer to store data that the program might not be able to process yet,  
but if you restart the program, some of the previous data is still in the buffer. So on start there might be some random data as a start point.  
Instead restarting matlab fully clears the buffer and gets rid of this problem  

![image](https://github.com/user-attachments/assets/bdbf100c-8b46-41d0-9539-5a2825e4acc4)  

  
![image](https://github.com/user-attachments/assets/64514818-4125-49dd-8c8d-c8d466dcc8c1)  
Blue is pitch (Up and down)    
tilting Away from you blue goes down (angle increases), towards you it goes up (angle decreases)  
Outputs angle as a radian
Red is roll (left and right)  
tilting Left makes red go up, right makes red go down  6
Shaking it gives the same effect as tilting because the it only checks accelleration  
Also Slight motion of the accelerometer adds 'noise' to the reading  
![image](https://github.com/user-attachments/assets/bc25fc3b-5d82-4d63-98fe-e421fc575e7b)

Gyroscope:  
Reduces effects of motion on the plot, giving a better reading for tilting  

Task 2  
When you shake the acceleration moves but not gyroscope.  
Gyroscope drifts due to the integration producing a 'dc offset'   
Accellerometer is moves more, but gyroscope is much more accurate  

Task 3:  
Low pass on accel to remove 'noise'  
high pass on accel to remove 'dc offset'  
![image](https://github.com/user-attachments/assets/ea00bef7-ea73-4f46-98de-eb6e0e726c85)

Task 4:  
30, 30 spacing centres 'Hello World!'  

Task 4 extra:  
Using Oled.Line instead as angle changes work better
Had to find pot.read() in python test code.  

Task 5:

Correctly Shifts when tilted
