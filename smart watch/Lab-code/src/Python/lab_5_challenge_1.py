# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:59:30 2020

@author: Anwar
"""

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

data_array = np.genfromtxt('appendix_a.csv', delimiter=',')#get data from Appendix A and save as .csv.




time = (data_array[:,0] - data_array[0,0])/1e6 #have time start at 0 and in seconds
HR = data_array[:,4]
"""def butter_lowpass(cutoff, fs, order):
    w = cutoff / (fs / 2)
    b, a = signal.butter(order, w, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y

b, a = butter_lowpass(filter_cutoff, fs, filter_order)
w, h = signal.freqz(b, a)

s_filt = butter_lowpass_filter(HR, filter_cutoff, fs, filter_order)"""

fs = 50

fc = 5  # Cut-off frequency of the filter
w = fc / (fs / 2) # Normalize the frequency
b, a = signal.butter(5, w, 'low')
output = signal.filtfilt(b, a, HR)



plt.figure(figsize = (10,10))
plt.subplot(3,2,(1,2))

w, h = signal.freqz(b,a)
plt.plot(w, 20 * np.log10(abs(h)))

plt.subplot(3,2,3)
plt.plot(time,HR)

plt.subplot(3,2,4)
plt.psd(data_array[:,4], NFFT=len(time), Fs=fs)


plt.subplot(3,2,5)
plt.plot(time,output)

plt.subplot(3,2,6)
plt.psd(output, NFFT=len(time), Fs=fs)


plt.show()