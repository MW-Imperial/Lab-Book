Task 1 = Dc motor and H bridge  
Each motor requires 2 directional pins and a PWM pin.  
We set up a timer to create a pwm, with a given frequency  
![image](https://github.com/user-attachments/assets/13da9633-284a-4ac8-8619-ba7edf302ae7)    
![image](https://github.com/user-attachments/assets/2bea24b9-dbdd-40a2-ad83-824ad12a705f)  
each motor can be controlled by choosing a direction and giving it a PWM (speed): 
![image](https://github.com/user-attachments/assets/1462aab7-2c77-4642-80b0-392b37f77ba2)

1b: potentiometer control:    
Used Linear interpolation to remap pot value into a motor duty cycle.  
![image](https://github.com/user-attachments/assets/762f9709-a4cc-4b05-8596-2ed699592894)  

Task 2: Polling Speed detection  
13 motor pole pairs and 1:30 gear ratio, so 390 pulses per revolution  
![image](https://github.com/user-attachments/assets/cf93e092-e85d-40f2-99ef-734e4cd645cf)  
we count number of rising edge transitions, there is a hardware polling rate that misses some of the counts.  
We check every 100ms to see how many counts, and display this speed as an rpm (divide by 39)  
Also added a line that rotates to show a spedometer
![image](https://github.com/user-attachments/assets/03ee6543-e0fb-45be-833d-0a0e9e777858)
The original code updated the display every loop, which added such a delay that it missed many of the counts, and gave a very low rpm  
Adding a delay causes the polling to miss many counts.    
![IMG_9959](https://github.com/user-attachments/assets/cd78bbb3-b9cd-4d44-a559-dc9ac87d0978)  
![IMG_9960](https://github.com/user-attachments/assets/b57f137a-4135-4a3a-a5a5-05ca35b9f096)  
![IMG_9961](https://github.com/user-attachments/assets/5eb4c132-4258-4934-a18a-f38c7e5a1d09)  



Task 3: Interrupt 
![image](https://github.com/user-attachments/assets/7d96b160-b045-4124-9a8d-17082bec8193)  
every time isr_motorA is called, it adds one to the count   
every time isr_speedtimer is called it updates the speed based on the count number, then resets the count number  
extint allows us to create our own interrupt  
motorA_int uses Y4 (hall effect) as an input, and checks it for rising edges, then runs isr_motorA  

every time speed time calls back, (every 100msec) it triggers isr_speedtimer  
![image](https://github.com/user-attachments/assets/372e826b-9316-4d4e-bd28-4a77c58d1b23)

3b:  
![IMG_9966](https://github.com/user-attachments/assets/69b69605-b52c-4d7f-962e-ed64ffee3464)
![image](https://github.com/user-attachments/assets/a63aa55f-40ec-499b-bb56-1eb1fffe9972)

![image](https://github.com/user-attachments/assets/261c986a-e333-45d1-89fb-34186c4f7a99)  
low rps seems to be that hard polling for the rising edges of hall effects is too slow to count all.  
characteristic is correct shape, motors will not start above a set pwm and motor b is slightly slower.  



