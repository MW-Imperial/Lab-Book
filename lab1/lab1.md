![nahidwincat](https://github.com/user-attachments/assets/103be7a3-8fd6-441d-aec5-bb953e62434f)
Lab 1  

Task 1  
sine_gen.m  
Creates a function for sin wave generation, it creates an array of time points from 0 to end  time T, with each interval corresponding to the sample frequency.  
Sig is each of these time points put into a sin function and multiplied by amplitude.  
![image](https://github.com/user-attachments/assets/4d093e58-caa0-49f3-b8f0-db3e29a7fe55)  
Learnt how to generate a sin wave and view it in matlab. It plots the first 200 sample values onto a graph to produces this:  
![image](https://github.com/user-attachments/assets/10558c2f-715f-4293-9655-f3ce2644f250)

Task 2  
plot_spec.m  
The plot spec function produces a frequency spectrum of the input sig  
First it Finds the magnitude of the fourier transform of the input signal, with as many frequency components as the input signal samples. the first harmonic frequency, df is fs over the number of samples in sig, N. Then it plots magnitude vs frequency.
![image](https://github.com/user-attachments/assets/6c220845-df14-4ff5-b791-8c95781c106b)

![image](https://github.com/user-attachments/assets/301932e1-6e0f-479b-9560-d4cc8a6ff81b)

Task 3  
Sig.mlx  
Waveform of both sinewaves combined:  
![image](https://github.com/user-attachments/assets/24a3e4ad-89e3-42dc-b41c-20a37719350d)  
Sigamp.mlx  
Waveform of amplitude  
![image](https://github.com/user-attachments/assets/981af629-08d5-4217-985b-94860b476c69)
shows both frequencies seperately.  

Task 4  
sigampnoise.mlx  
![image](https://github.com/user-attachments/assets/59216b8d-3792-40bf-bea8-41b465cf1b82)
![image](https://github.com/user-attachments/assets/4fe13bd5-1714-490b-8f3f-94e4f5fec7c9)  
randn(size(sig)) returns an array of random numbers, same length as the signal.  
  
Adding noise adds some amplitude to all frequencies, making the regular wave a lot harder to read,  
but the frequency graph can still clearly show the dominant frequencies    
noise has much less energy as it is spread over a longer range, so it has less magnitude in the spectrum plot.  

Task 5  
dotproduct.mlx  
S1xS2 gives a result of: dot_product = 3.6526e-13  
S1xS3 gives dot_product2 = -1.9668e-10  
which is a larger number, because the frequencies are closer.  
(S1+S2)XS1 gives dot_product3 = 5.0000e+03  
This is a much larger number because there is a large component of s1 being projected onto itself  

![image](https://github.com/user-attachments/assets/282339ef-f8ae-4033-80dc-9c3348c39e65)

