# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 14:53:05 2020

@author: Anwar
"""


import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

gnd = np.array([75, 74, 73, 74, 80, 82, 87, 90 ,98, 69]) #reference heart rate
est = np.array([72, 90, 78, 78, 84, 90, 72, 96, 84, 78]) #estimate of your algorithm

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
