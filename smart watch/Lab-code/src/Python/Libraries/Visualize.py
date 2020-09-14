#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:21:58 2020

@author: edwardwang
"""
import matplotlib.pyplot as plt


class Visualize:


    
    def plotData(self,data_array):
        time = data_array[:,0]
        x = data_array[:,1]
        y = data_array[:,2]
        z = data_array[:,3]
        IR = data_array[:,4]

    
   
  
    
        plt.clf()
        plt.subplot(411)
        plt.title('Example Data plot', fontsize=10)#plt.subplot(311)
        plt.plot(time,x) #fill in ax and ay
        plt.ylabel("x Amplitude")

        plt.subplot(412)
        plt.plot(time,y) #fill in bx and by
        plt.ylabel("y Amplitude")
    
        plt.subplot(413)
        plt.plot(time,z)
        plt.ylabel("z Amplitude")
    

    
        plt.subplot(414)
        plt.plot(time,IR)
        plt.ylabel("IR Amplitude")
        plt.xlabel(u'Time(${\mu}s$)')#plot the 3 axis accelerometer data and the heart pulse data into 4 subplots
        
    def plotAccel(data_array):
        # plot the 3 axis accelerometer data
        time = data_array[:,0]
        x = data_array[:,1]
        y = data_array[:,2]
        z = data_array[:,3]
        
        
        plt.clf()
        plt.subplot(311)
        plt.title('Example Data plot', fontsize=10)#plt.subplot(311)
        plt.plot(time,x) #fill in ax and ay
        plt.ylabel("x Amplitude")

        plt.subplot(312)
        plt.plot(time,y) #fill in bx and by
        plt.ylabel("y Amplitude")
    
        plt.subplot(313)
        plt.plot(time,z)
        plt.ylabel("z Amplitude")
        
        
    def plotHr(data_array):
        # plot the heart pulse data
        time = data_array[:,0]
        IR = data_array[:,4]
        
        
        plt.plot(time,IR)
        plt.ylabel("IR Amplitude")
        plt.xlabel(u'Time(${\mu}s$)')