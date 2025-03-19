Task 1: Moving average filter  
4 tap:    
![image](https://github.com/user-attachments/assets/1585494f-95aa-4eb5-881f-81b90081dc28)  
![image](https://github.com/user-attachments/assets/e552b5d7-4429-4509-a868-6a906bf7ec7f)  
Filtered verssion on the left, slight reduction of noise can be seen by thinner and slightly lower peaks.  

Changing for variable taps:  
![image](https://github.com/user-attachments/assets/5302da8c-f689-4d1d-b5a5-a3a782342e82)  
for each x value, a temp is stored, then all x values up to N, number of taps below are summed with a for loop.  
Then it is divided by number of taps to find the average  
10 tap:  
![image](https://github.com/user-attachments/assets/2931ca3e-89e6-4172-a858-9f3cdce7a804)

20 tap:  
![image](https://github.com/user-attachments/assets/86eaec32-1b85-4ae0-a9fa-b2451af07fed)  

50 tap:  
![image](https://github.com/user-attachments/assets/5707ff88-8bdb-421a-952c-445e340da4f2)  

Task 2: Microphone class  
![image](https://github.com/user-attachments/assets/6fa0f9b6-a4e4-4b11-a729-6acb071b536f)  
mic class creates a buffer array that starts at 0
It also sets up an interrupt timer based on input timer.  

DC offsett is around 1523 - subtracted from signal to correct it.  
uses a pointer with wrap around to work out where it is in the buffer array and finish the interrupt if the buffer is full.   
it also works out sum of squares to find energy. 

![image](https://github.com/user-attachments/assets/b9c1c0bd-4f18-4dca-b74b-eb353b03c60f)  

Task 3: 
