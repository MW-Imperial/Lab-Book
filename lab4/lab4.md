Task 1: The inertial Measurement Unit (MU)
![image](https://github.com/user-attachments/assets/bdbf100c-8b46-41d0-9539-5a2825e4acc4)


![image](https://github.com/user-attachments/assets/64514818-4125-49dd-8c8d-c8d466dcc8c1)
Blue is pitch:
Away from you blue goes down, towards you it goes up
Red is roll:
Left makes red go up, right makes red go down
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

