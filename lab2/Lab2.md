Lab 2 Book  

Task 1  
Step 1:  
![image](https://github.com/user-attachments/assets/6245d45c-bff1-4b9d-9a72-4e6cae8bb02a)  

Successfully connected the pybench, and accessed the files  
image of pybench  
![image](https://github.com/user-attachments/assets/ec61e8be-bf11-4fac-9135-80d0a07584b0)
![image](https://github.com/user-attachments/assets/89451742-eab6-41b4-8723-1c91d3413bfb)    
![image](https://github.com/user-attachments/assets/c1e81610-15d6-4ab7-b806-c81e71448e2c)

Step 2:  
![image](https://github.com/user-attachments/assets/3c324330-e828-4801-b047-b3fb10ca00d2)  

Checked and all test features worked fine  

Step 3:  
Matlab path setup worked, and pb returned expected properties  
First the code searches for a list of serial ports on the computer,  
![image](https://github.com/user-attachments/assets/885e201c-3311-425d-984a-c2124f35f8b5)  
  Then the last port 'ports(end)' is usually the one we access for the pybench. 
![image](https://github.com/user-attachments/assets/cb6009f0-ba47-4170-9a75-f7047b41a19a)  
  Finally we create a pb object by calling the pybench  
![image](https://github.com/user-attachments/assets/25fb9d9f-45ae-4c41-9223-2ba9521f9091)    

when you do pb.set_max_v(2.5) the following happens:  
1. PC sends 3 bytes to pybench as serial data via USB. First is a command, followed by the value of voltage as two bytes. first byte is int(4096*(v/3.3)/256) and second is (4096*(v/3.3)) mod 256.  
2. pybench.py runs on the board (blue LED ON, waiting for the signal. Known as polling  
3. When it receives the bytes, the code sets the max voltage of the ADC to 2.5v.


Task 2:  
![image](https://github.com/user-attachments/assets/955c021d-d563-45f8-8e96-ddcd4d925d60)   
pb changes the properties of the output signal sine wave, pb.sine() 
The code generates the signal and then captures it back again as the analogue output is shorted to the input.  
![image](https://github.com/user-attachments/assets/9c9871fa-d45f-4511-9225-a908bd6cb4a4)

plot('o') plots just the sample points on figure 1,  
plot() does a continous wave  
and figure 2 shows frequency domain  
data = samples - mean(samples) removes the DC offset.  

Task 3:  
The first code produces a single instant of the noise put into the microphone, and its frequency spectrum 
![image](https://github.com/user-attachments/assets/816a0c58-4f85-45cc-bc4f-c3ab06132f77)

when the loop is added the file continuosly updates, and when the input frequency is increased it goes up on the frequency spectrum  

above 4900hz (half fs) it begins to fold down to lower frequencies.  

  
task 4:  
converting to dB shows the lower amplitude much clearer than a linear scale  

1000 Hz  
<img width="359" alt="image" src="https://github.com/user-attachments/assets/c7fdc7ac-e163-4cd3-b2d0-4cce1750c1e3" />
 

1100 Hz   
![image](https://github.com/user-attachments/assets/c726d15f-3341-459a-981c-182e6eaccd96)  

hamming  

makes the peak sharper by multiplying the frequency we want by a hamming window:  
![image](https://github.com/user-attachments/assets/b91900f9-ccf7-4ffe-a297-5c7dd257f65e)  
<img width="408" alt="image" src="https://github.com/user-attachments/assets/d8f1bc19-483f-418b-9f59-d359e51715e6" />  
<img width="396" alt="image" src="https://github.com/user-attachments/assets/c5eef5bc-28de-4d08-906b-28fa774ce122" />  
<img width="405" alt="image" src="https://github.com/user-attachments/assets/e0036a6b-e298-4075-8335-eff362f05149" />  



Task 5: 2 dominant frequencies  
1.07  
11.56  
<img width="225" alt="image" src="https://github.com/user-attachments/assets/024fbbb2-6529-445f-ae42-8cfe2ccfa58b" />  
<img width="254" alt="image" src="https://github.com/user-attachments/assets/243eaea8-68d4-4732-9966-bc8ced0fc366" />  
<img width="248" alt="image" src="https://github.com/user-attachments/assets/be4aec72-9b7e-43a6-9b1e-7bcaf3c1f621" />  



2.17  
9.44  


Task 6:  
Audio wav were different lengths, so cropped each to the length of the shorter one, then added them together.  
Analysis of the combined signal showed a clear bass freq and higher guitar frequencies.  

1.
<img width="348" alt="Screenshot 2025-01-23 at 11 44 16" src="https://github.com/user-attachments/assets/a6e371bb-58d1-4c66-a678-d918d5dd9b94" />    
      
2.
<img width="373" alt="Screenshot 2025-01-23 at 11 44 29" src="https://github.com/user-attachments/assets/59cbde32-c416-4061-a740-b05c02a4594a" />      
     
3.
<img width="357" alt="Screenshot 2025-01-23 at 11 44 37" src="https://github.com/user-attachments/assets/99c117ba-ca5a-4e5e-8df6-afb9b788c03c" />      
     

