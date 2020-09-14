# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 17:33:42 2020

@author: Anwar
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.stats import pearsonr



data_array1 = np.genfromtxt('Data_01_075.csv', delimiter=',')
data_array2 = np.genfromtxt('Data_02_074.csv', delimiter=',')
data_array3 = np.genfromtxt('Data_03_073.csv', delimiter=',')
data_array4 = np.genfromtxt('Data_04_074.csv', delimiter=',')
data_array5 = np.genfromtxt('Data_05_080.csv', delimiter=',')
data_array6 = np.genfromtxt('Data_06_082.csv', delimiter=',')
data_array7 = np.genfromtxt('Data_07_087.csv', delimiter=',')
data_array8 = np.genfromtxt('Data_08_090.csv', delimiter=',')
data_array9 = np.genfromtxt('Data_09_98.csv', delimiter=',')
data_array10 = np.genfromtxt('Data_10_069.csv', delimiter=',')


time1 = (data_array1[:,0] - data_array1[0,0])/1e6 #have time start at 0 and in seconds
time2 = (data_array2[:,0] - data_array2[0,0])/1e6
time3 = (data_array3[:,0] - data_array3[0,0])/1e6
time4 = (data_array4[:,0] - data_array4[0,0])/1e6
time5 = (data_array5[:,0] - data_array5[0,0])/1e6
time6 = (data_array6[:,0] - data_array6[0,0])/1e6
time7 = (data_array7[:,0] - data_array7[0,0])/1e6
time8 = (data_array8[:,0] - data_array8[0,0])/1e6
time9 = (data_array9[:,0] - data_array9[0,0])/1e6
time10 = (data_array10[:,0] - data_array10[0,0])/1e6


def moving_average(s,n_avg):
    
        ma = np.zeros(s.size) #previously np.array(s.size) that was incorrect, sorry
        for i in np.arange(0,len(s)):
            ma[i] = np.mean(s[i:i+n_avg])#mean of s from index i to i+n_avg
        return s - ma

Pxx, Freqs = plt.psd(moving_average(data_array1[:,4],5), NFFT=len(time1), Fs=45) #plot the power spectral density

freq1 = Freqs[12]
heartrate = freq1 * 60
print("heartrate1:", heartrate)

Pxx, Freqs = plt.psd(moving_average(data_array2[:,4],5), NFFT=len(time2), Fs=45) #plot the power spectral density

freq2 = Freqs[11]
heartrate = freq2 * 60
print("heartrate2:", heartrate)

Pxx, Freqs = plt.psd(moving_average(data_array3[:,4],5), NFFT=len(time3), Fs=45) #plot the power spectral density
freq3 = Freqs[12]
heartrate = freq3 * 60
print("heartrate3:", heartrate)

Pxx, Freqs = plt.psd(moving_average(data_array4[:,4],5), NFFT=len(time4), Fs=45) #plot the power spectral density
freq4 = Freqs[12]
heartrate = freq4 * 60
print("heartrate4:", heartrate)

Pxx, Freqs = plt.psd(moving_average(data_array5[:,4],5), NFFT=len(time5), Fs=45) #plot the power spectral density

freq5 = Freqs[15]
heartrate = freq5 * 60
print("heartrate5:", heartrate)

Pxx, Freqs = plt.psd(moving_average(data_array6[:,4],5), NFFT=len(time6), Fs=45) #plot the power spectral density
freq6 = Freqs[9]
heartrate = freq6 * 60
print("heartrate6:", heartrate)

Pxx, Freqs = plt.psd(moving_average(data_array7[:,4],5), NFFT=len(time7), Fs=45) #plot the power spectral density
freq7 = Freqs[17]
heartrate = freq7 * 60
print("heartrate7:", heartrate)

Pxx, Freqs = plt.psd(moving_average(data_array8[:,4],5), NFFT=len(time8), Fs=45) #plot the power spectral density
freq8 = Freqs[18]
heartrate = freq8 * 60
print("heartrate8:", heartrate)

Pxx, Freqs = plt.psd(moving_average(data_array9[:,4],5), NFFT=len(time9), Fs=45) #plot the power spectral density

freq9 = Freqs[15]
heartrate = freq9 * 60
print("heartrate9:", heartrate)

Pxx, Freqs = plt.psd(moving_average(data_array10[:,4],5), NFFT=len(time10), Fs=45) #plot the power spectral density
plt.plot(Freqs,Pxx)
freq10 = Freqs[12]
heartrate = freq10 * 60
print("heartrate10:", heartrate)


print("freq1",freq1)
print("freq2",freq2)
print("freq3",freq3)
print("freq4",freq4)
print("freq5",freq5)
print("freq6",freq6)
print("freq7",freq7)
print("freq8",freq8)
print("freq9",freq9)
print("freq10",freq10)











"""plt.figure(figsize = (12,30))
plt.subplot(10,2,1)
plt.plot(time1,moving_average(data_array1[:,4],5))

plt.subplot(10,2,2)
Pxx, Freqs = plt.psd(moving_average(data_array1[:,4],5), NFFT=len(time1), Fs=45) #plot the power spectral density

freq1 = Freqs[np.argmax(Pxx)]
print("Fundamental freq1",freq1)

heartrate = freq1 * 60

print("heartrate1:", heartrate)


plt.subplot(10,2,3)
plt.plot(time2,moving_average(data_array2[:,4],5))

plt.subplot(10,2,4)
Pxx, Freqs = plt.psd(moving_average(data_array2[:,4],5), NFFT=len(time2), Fs=45) #plot the power spectral density

freq2 = Freqs[np.argmax(Pxx)]
print("Fundamental freq2",freq2)

heartrate = freq2 * 60
print("heartrate2:", heartrate)


plt.subplot(10,2,5)
plt.plot(time3,moving_average(data_array3[:,4],5))

plt.subplot(10,2,6)
Pxx, Freqs = plt.psd(moving_average(data_array3[:,4],5), NFFT=len(time3), Fs=45) #plot the power spectral density

freq3 = Freqs[np.argmax(Pxx)]
print("Fundamental freq3",freq3)

heartrate = freq3 * 60
print("heartrate3:", heartrate)

plt.subplot(10,2,7)
plt.plot(time4,moving_average(data_array4[:,4],5))

plt.subplot(10,2,8)
Pxx, Freqs = plt.psd(moving_average(data_array4[:,4],5), NFFT=len(time4), Fs=45) #plot the power spectral density

freq4 = Freqs[np.argmax(Pxx)]
print("Fundamental freq4",freq4)

heartrate = freq4 * 60
print("heartrate4:", heartrate)

plt.subplot(10,2,9)
plt.plot(time5,moving_average(data_array5[:,4],5))

plt.subplot(10,2,10)
Pxx, Freqs = plt.psd(moving_average(data_array5[:,4],5), NFFT=len(time5), Fs=45) #plot the power spectral density

freq5 = Freqs[np.argmax(Pxx)]
print("Fundamental freq5",freq5)

heartrate = freq5 * 60
print("heartrate5:", heartrate)

plt.subplot(10,2,11)
plt.plot(time6,moving_average(data_array6[:,4],5))


plt.subplot(10,2,12)
Pxx, Freqs = plt.psd(moving_average(data_array6[:,4],5), NFFT=len(time6), Fs=45) #plot the power spectral density

freq6 = Freqs[np.argmax(Pxx)]
print("Fundamental freq6",freq6)

heartrate = freq6 * 60
print("heartrate6:", heartrate)

plt.subplot(10,2,13)
plt.plot(time7,moving_average(data_array7[:,4],5))

plt.subplot(10,2,14)
Pxx, Freqs = plt.psd(moving_average(data_array7[:,4],5), NFFT=len(time7), Fs=45) #plot the power spectral density

freq7 = Freqs[np.argmax(Pxx)]
print("Fundamental freq7",freq7)

heartrate = freq7 * 60
print("heartrate7:", heartrate)

plt.subplot(10,2,15)
plt.plot(time8,moving_average(data_array8[:,4],5))

plt.subplot(10,2,16)
Pxx, Freqs = plt.psd(moving_average(data_array8[:,4],5), NFFT=len(time8), Fs=45) #plot the power spectral density

freq8 = Freqs[np.argmax(Pxx)]
print("Fundamental freq8",freq8)

heartrate = freq8 * 60
print("heartrate8:", heartrate)

plt.subplot(10,2,17)
plt.plot(time9,moving_average(data_array9[:,4],5))

plt.subplot(10,2,18)
Pxx, Freqs = plt.psd(moving_average(data_array9[:,4],5), NFFT=len(time9), Fs=45) #plot the power spectral density
freq9 = Freqs[np.argmax(Pxx)]
print("Fundamental freq9",freq9)

heartrate = freq9 * 60
print("heartrate9:", heartrate)

plt.subplot(10,2,19)
plt.plot(time10,moving_average(data_array10[:,4],5))

plt.subplot(10,2,20)
Pxx, Freqs = plt.psd(moving_average(data_array10[:,4],5), NFFT=len(time10), Fs=45) #plot the power spectral density
freq10 = Freqs[np.argmax(Pxx)]
print("Fundamental freq10",freq10)

heartrate = freq10 * 60
print("heartrate10:", heartrate)"""


gnd = np.array([71, 104, 92, 66, 85, 67, 70, 67 ,65, 90]) #reference heart rate
est = np.array([78, 120, 102, 60, 96, 60, 78, 60, 54, 90]) #estimate of your algorithm


[R,p] = pearsonr(gnd,est)

plt.figure(1)
plt.clf()
plt.subplot(121)
plt.plot(gnd,gnd)
plt.scatter(gnd,est)
plt.text(min(gnd) + 2,max(est)+2,"R="+str(round(R,2)))
plt.ylabel("estimate HR (BPM)")
plt.xlabel("reference HR (BPM)")

avg = np.mean( np.array([ gnd, est ]), axis=0 )#take the average of gnd and est

dif = est - gnd#take the difference of gnd and est

std = np.std(est)#get the standard deviation of the difference (using np.std)

bias = np.mean(dif)#the mean value of the difference
print(bias)

upper_std = (bias + 1.96) * std#the bias plus 1.96 times the std

lower_std = (bias - 1.96) * std#the bias minus 1.96 times the std


plt.subplot(122)
plt.scatter(avg, dif)
plt.plot([np.min(avg),np.max(avg)],[bias,bias])
plt.plot([np.min(avg),np.max(avg)],[upper_std, upper_std])
plt.plot([np.min(avg),np.max(avg)],[lower_std, lower_std])
plt.text(np.max(avg)+5,bias,"mean="+str(round(np.mean(gnd-est),2)))
plt.text(np.max(avg)+5,upper_std,"1.96STD="+str(round(upper_std,2)))
plt.text(np.max(avg)+5,lower_std,"-1.96STD="+str(round(lower_std,2)))
plt.ylabel("Difference of Est and Gnd (BPM)")
plt.xlabel("Average of Est and Gnd (BPM)")
plt.show()





plt.show()
