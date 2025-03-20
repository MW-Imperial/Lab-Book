Challenge 1: dancing led strip  
Done at the end of lab 6  

Challenge 2: control speed of motors usig IMU:  

![image](https://github.com/user-attachments/assets/af682e23-90ae-4c48-ba27-34315073af0e)  

code functions same as potentiometer read code, but instead mapping the pitch and roll angles.  
A complementary filter is used to gain more accurate results.  


Challenge 5: Self balancing segway  

Code explanation:  
Initial variables and imports: 
![image](https://github.com/user-attachments/assets/cdbaceee-6cfd-4912-80be-9c1bdaf6dae3)  
Setting up motors:  
![image](https://github.com/user-attachments/assets/82129ad3-bd55-42ba-bca9-ba840d66693a)  
  defined a complementary filter function that gave a better estimate of pitch angle, updating a global variable.  
Pitch dot seemed innacurate when used inside the function, so was not used globally.  
Tuning coefficients:  
![image](https://github.com/user-attachments/assets/d608d3dd-682f-4014-82c3-f156d849110f)    
Once we found the coefficients with the potentiometer the example code was replaced to just have the variables 
PID control:  
![image](https://github.com/user-attachments/assets/067af50b-960b-4f26-a7ec-bdf0cde996da)  
This used less lines of code than a class
  
Troubleshooting:  
print statements were written line by line in order to determine the errors in the code  
One major error is that tic was in millis and toc in micros, causing dt to be 1,000,000x greater than it should  
we also did not convert to seconds when using dt in the complementary filter.

Also we had to optimise the code to reduce dt, as multiplying it by the integration error sum was too large and meant ki scaling way too powerful  

adding to the code:  
introduced a decay function to ki as if it spent to much time on one side the ki could never recover and it fell over  
the decay means that newer values are prioritised   


Tuning:
our kp was much more powerful than expected, so we ended up in a range of 1-2.5 and settled on 2.2
Then tuned kd to reduce the period of oscillations, but too high and it vibrated really fast whilst balancing, so 0.7 was chosen.
Ki was set as high as possible as the error sum was not strong enough, so 150 was chosen.

Results:  
Kp 2.2  
Ki 150  
Kd 0.7  

