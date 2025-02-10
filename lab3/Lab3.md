Task 1  
1.5v ->1.74 v  
0v -> 0.02  
<img width="1512" alt="Screenshot 2025-02-06 at 11 27 33" src="https://github.com/user-attachments/assets/a096ce00-b909-438e-adfd-0b14965e4d40" />
<img width="1263" alt="Screenshot 2025-02-06 at 11 27 39" src="https://github.com/user-attachments/assets/aa380f02-d696-4a10-891c-c99491bb8107" />
min is about 0.4v  - bulb requires some power to heat up so doesn't output light until about 0.4v  
<img width="1185" alt="Screenshot 2025-02-06 at 11 29 45" src="https://github.com/user-attachments/assets/4023da4c-29be-45de-b31a-6082fde8caaf" />  
max is 1.68v  
Why does it plateau? The circuit cannot recieve higher voltages, so it caps out at around 1.68v  
<img width="1252" alt="Screenshot 2025-02-06 at 11 29 31" src="https://github.com/user-attachments/assets/8397514a-bb05-49ce-85fe-7bee011913c0" />  

Missing curve img???  
Curve is exponential as p= V^2/R  
Why does it oscillate? The circuit is made up of 4 op amps which create a simulated second order ODE.  

linear at 1.45-1.55v  
if it was fully linear it would look like a straight line graph  
the gradient gives the gain of the system.  

Task 2  
Peaks at 5hz which is the frequency of ODE oscillation:    
<img width="361" alt="Screenshot 2025-02-06 at 11 55 40" src="https://github.com/user-attachments/assets/11cf20ff-0796-499e-960c-2c7e9267847c" />
<img width="342" alt="Screenshot 2025-02-06 at 11 51 15" src="https://github.com/user-attachments/assets/289b7697-68bc-4213-a665-4810125ae077" />

Manual Calculation using G(s):  
Starts at (0,0)  
5Hz -> 12.2dB  
20Hz -> -37.1743dB  


Task 3  
![image](https://github.com/user-attachments/assets/147e39f5-a88d-4db8-967f-55698d20bcb5)<img width="371" alt="Screenshot 2025-02-06 at 11 58 35" src="https://github.com/user-attachments/assets/42a8252e-c7d3-46b8-a19e-7f159ec21570" />
<img width="377" alt="Screenshot 2025-02-06 at 11 58 07" src="https://github.com/user-attachments/assets/ee8f38f6-782b-4e64-95fc-2e3763103812" />
<img width="369" alt="Screenshot 2025-02-06 at 11 57 39" src="https://github.com/user-attachments/assets/8a824e2d-fdee-4a73-b2de-e897c1034fbc" />
<img width="399" alt="Screenshot 2025-02-06 at 11 57 19" src="https://github.com/user-attachments/assets/f6d9752a-b25e-4bff-bfb9-a78bdbd77bf4" />
<img width="373" alt="Screenshot 2025-02-06 at 11 57 00" src="https://github.com/user-attachments/assets/0d8f68d3-ed1c-479d-ab11-2eba9202ca01" />

<img width="362" alt="Screenshot 2025-02-06 at 12 05 36" src="https://github.com/user-attachments/assets/99e65e92-c684-453a-b110-cf93c4d60f6d" />    
Also peaks at 5Hz at 12dB higher gain, which correlates to multiplier from lightbulb characteristic graph gain in 1.45-1.55v range. (gradient of ???)     

Task 4 ???  
oscillates at 5Hz  
Step up has a higher amplitude of oscillation as it is in high gain range of lightbulb characteristic  
Step down has lower gain, so lower amplitude can be seen:
<img width="339" alt="Screenshot 2025-02-06 at 12 07 46" src="https://github.com/user-attachments/assets/0914ed11-89c0-49eb-8e44-feb722a7092e" />
