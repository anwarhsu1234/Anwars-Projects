# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:51:17 2020

@author: Anwar
"""
import numpy as np
class Heartrate:
    
    
    
    def calc_heart_rate_time(self,signal):
        count = 0
        state = 0
        threshold = .6
        
        for value in signal:
            if state == 0:
                if value > threshold:
                    count += 1
                    state = 1
                
            if value < threshold:
                state = 0
        print("count",count)
        return count * 6 #Calculate the beats per minute. 


    def calc_heart_rate_freq(signal,fs):
        
        Pxx, Freqs = plt.psd(signal, NFFT=len(self.Wearable.time), Fs=fs)
        

    def normalize_signal(self,signal):
        min = -1000#find min of signal
        signal = signal - min#subtract the minimum so the minimum of the signal is zero
        max =1800#find the new maximum of the signal
        norm_signal = signal / max#divide the signal by the new maximum so the maximum becomes 1
        return norm_signal 


    def moving_average(self,s,n_avg):
    
        ma = np.zeros(s.size) #previously np.array(s.size) that was incorrect, sorry
        for i in np.arange(0,len(s)):
            ma[i] = np.mean(s[i:i+n_avg])#mean of s from index i to i+n_avg
        return s - ma