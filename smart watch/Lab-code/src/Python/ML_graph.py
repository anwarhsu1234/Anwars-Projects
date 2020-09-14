# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:00:07 2020

@author: Anwar
"""

import glob
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture as GMM
from scipy.stats import pearsonr


list_ref = np.genfromtxt('list_ref.csv', delimiter=',')
H = np.genfromtxt('heart.csv', delimiter=',')
H1 = np.genfromtxt('heart1.csv', delimiter=',')
H2 = np.genfromtxt('heart2.csv', delimiter=',')
H3 = np.genfromtxt('heart3.csv', delimiter=',')
H4 = np.genfromtxt('heart4.csv', delimiter=',')
H5 = np.genfromtxt('heart5.csv', delimiter=',')
H6 = np.genfromtxt('heart6.csv', delimiter=',')
H7 = np.genfromtxt('heart7.csv', delimiter=',')
heartrate = np.concatenate((H,H1,H2,H3,H4,H5,H6,H7))





gnd = np.array(list_ref)#reference heart rate
est = np.array(heartrate)#estimate of your algorithm

[R,p] = pearsonr(gnd,est)

plt.figure(1)
plt.clf()
plt.subplot(121)
plt.plot(gnd,gnd)
plt.scatter(gnd,est)
plt.text(min(gnd) + 2,max(est)+2,"R="+str(round(R,2)))
plt.ylabel("estimate HR (BPM)")
plt.xlabel("reference HR (BPM)")

avg =  np.mean( np.array([ gnd, est ]), axis=0 )#take the average of gnd and est
dif = est - gnd#take the difference of gnd and est
std = np.std(est)#get the standard deviation of the difference (using np.std)
bias = np.mean(dif)#the mean value of the difference
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

    
    
    