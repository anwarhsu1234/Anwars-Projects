# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:52:15 2020

@author: Anwar
"""
import numpy as np
import matplotlib.pyplot as plt

data_array1 = np.genfromtxt('Data_01_075.csv', delimiter=',')
time1 = (data_array1[:,0] - data_array1[0,0])/1e6

def moving_average(s,n_avg):
    
        ma = np.zeros(s.size) #previously np.array(s.size) that was incorrect, sorry
        for i in np.arange(0,len(s)):
            ma[i] = np.mean(s[i:i+n_avg])#mean of s from index i to i+n_avg
        return s - ma
    
Pxx, Freqs = plt.psd(moving_average(data_array1[:,4],5), NFFT=len(time1), Fs=45) #plot the power spectral density
freq = Freqs[np.argmax(Pxx)]

heartrate = freq * 60

print("heartrate:", heartrate)