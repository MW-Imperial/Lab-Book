Lab 2 Book  

Task 1  
Step 1:  
![image](https://github.com/user-attachments/assets/6245d45c-bff1-4b9d-9a72-4e6cae8bb02a)  

Successfully connected the pybench, and accessed the files  
image of pybench  
![image](https://github.com/user-attachments/assets/89451742-eab6-41b4-8723-1c91d3413bfb)    

Step 2:  
![image](https://github.com/user-attachments/assets/3c324330-e828-4801-b047-b3fb10ca00d2)  

Checked and all test features worked fine  

Step 3:  
Matlab path setup worked, and pb returned expected properties  
![image](https://github.com/user-attachments/assets/25fb9d9f-45ae-4c41-9223-2ba9521f9091)  

Task 2:  
![image](https://github.com/user-attachments/assets/955c021d-d563-45f8-8e96-ddcd4d925d60)   
pb changes the properties of the output signal sine wave,  
plot('o') plots just the sample points on figure 1,  
plot() does a continous wave  
and figure 2 shows frequency domain  

Task 3:  
The first code produces a single instant of the noise put into the microphone, and its frequency spectrum  
when the loop is added the file continuosly updates, and when the input frequency is increased it goes up on the frequency spectrum  

task 4:  
1000  
![image](https://github.com/user-attachments/assets/885c4189-9aa5-4716-96cf-bb1abbaeb021)  

1100  
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

<img width="348" alt="Screenshot 2025-01-23 at 11 44 16" src="https://github.com/user-attachments/assets/a6e371bb-58d1-4c66-a678-d918d5dd9b94" />  
<img width="373" alt="Screenshot 2025-01-23 at 11 44 29" src="https://github.com/user-attachments/assets/59cbde32-c416-4061-a740-b05c02a4594a" />  
<img width="357" alt="Screenshot 2025-01-23 at 11 44 37" src="https://github.com/user-attachments/assets/99c117ba-ca5a-4e5e-8df6-afb9b788c03c" />  


