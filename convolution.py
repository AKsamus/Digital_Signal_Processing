import scipy.signal as signal
from commfun import si

import numpy as np
import matplotlib.pyplot as plt

ll=0
ul=10
t = np.arange(ll-2, ul+3) # Range for the impulse response
def val_h(n):
    if n < ll or n > ul:
        return 0 
    si_val = 0.5*si((np.pi*0.5)*(n-5))
    return si_val
# Define the input signal (e.g., a step function)
x = np.array([1]*7+[0]*8)  # Step function: 1 for the first 4 samples, then 0

# Define the impulse response of the system (e.g., a simple low-pass filter)
h = np.array([val_h(n) for n in range(ll-2, ul+3)])

# Perform convolution
output_signal = signal.convolve(x, h, mode='full')[:len(t)]  
print("Input Signal (x):", x)
print("Impulse Response (h):", h)
print("Output Signal (y):", output_signal)

# Plotting the input signal, impulse response, and output signal
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.stem(t,x)
plt.title(' u(k-x)')
plt.subplot(3, 1, 2)
plt.stem(t, h)
plt.title('h(x)')
plt.subplot(3, 1, 3)
plt.stem(t, output_signal)
plt.title('Output Signal (y)')
plt.tight_layout()
plt.show()

