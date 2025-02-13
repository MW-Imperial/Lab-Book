Lab 1  

Task 1  
![image](https://github.com/user-attachments/assets/197098b8-0169-4f84-86b2-03012dc54873)

sine_gen.m  
Creates a function for sin wave generation, it creates an array of time points from 0 to end  time T, with each interval corresponding to the sample frequency.  
Sig is each of these time points put into a sin function and multiplied by amplitude.  
![image](https://github.com/user-attachments/assets/4d093e58-caa0-49f3-b8f0-db3e29a7fe55)  
Learnt how to generate a sin wave and view it in matlab. It plots the first 200 sample values onto a graph to produces this:  
![image](https://github.com/user-attachments/assets/10558c2f-715f-4293-9655-f3ce2644f250)

Task 2  
![image](https://github.com/user-attachments/assets/86995d3d-14af-4f79-a145-c79bcd3d5700)

plot_spec.m  
The plot spec function produces a frequency spectrum of the input sig  
First it Finds the magnitude of the fourier transform of the input signal, with as many frequency components as the input signal samples. the first harmonic frequency, df is fs over the number of samples in sig, N. Then it plots magnitude vs frequency.
![image](https://github.com/user-attachments/assets/6c220845-df14-4ff5-b791-8c95781c106b)

![image](https://github.com/user-attachments/assets/301932e1-6e0f-479b-9560-d4cc8a6ff81b)

Task 3  
![image](https://github.com/user-attachments/assets/402ba2cb-6762-4bbd-b562-be4ecda6240a)

Sig.mlx  
Waveform of both sinewaves combined:  
![image](https://github.com/user-attachments/assets/24a3e4ad-89e3-42dc-b41c-20a37719350d)  
Sigamp.mlx  
Waveform of amplitude  
![image](https://github.com/user-attachments/assets/981af629-08d5-4217-985b-94860b476c69)  
shows both frequencies seperately.  

Task 4  
![image](https://github.com/user-attachments/assets/6ec5fea3-6118-49fd-afb0-8c486a7e073b)

sigampnoise.mlx  
![image](https://github.com/user-attachments/assets/59216b8d-3792-40bf-bea8-41b465cf1b82)
![image](https://github.com/user-attachments/assets/4fe13bd5-1714-490b-8f3f-94e4f5fec7c9)  
randn(size(sig)) returns an array of random numbers, same length as the signal.  
  
Adding noise adds some amplitude to all frequencies, making the regular wave a lot harder to read,  
but the frequency graph can still clearly show the dominant frequencies    
noise has much less energy as it is spread over a longer range, so it has less magnitude in the spectrum plot.  

Task 5  
![image](https://github.com/user-attachments/assets/611cae4e-784b-4e60-8b89-ba7c6852f5fc)

dotproduct.mlx  
S1xS2 gives a result of: dot_product = 3.6526e-13  
S1xS3 gives dot_product2 = -1.9668e-10  
which is a larger number, because the frequencies are closer, but still minute as the frequencies are orthogonal / have nothing in common with each other
(S1+S2)XS1 gives dot_product3 = 5.0000e+03  
This is a much larger number because there is a large component of s1 being projected onto itself, and the magnitude multiplies with itself through the dot product.  

![image](https://github.com/user-attachments/assets/282339ef-f8ae-4033-80dc-9c3348c39e65)

Task 6  
![image](https://github.com/user-attachments/assets/9c517f83-9b41-4148-83b9-9ad232447030)
![image](https://github.com/user-attachments/assets/939f5d9d-0e4d-4781-a8c0-473cbd1f42e1)  #
Shows the Spectrum changing with tune  

