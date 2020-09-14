# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 20:11:20 2020

@author: Anwar
"""
import numpy as np
class Data:
    
    def __init__(self):
        self.data_array = np.array([])
        
    
    def add_data(self,new_data):
        self.counter = 0
        
        if(self.data_array.size == 0): 
            self.data_array = new_data
        else:
            self.data_array = np.vstack((self.data_array,new_data))
            # print(len(self.data_array))
            if len(self.data_array) == 500:
                print("sampling rate:",self.calc_sampling_rate())
                np.savetxt("data.csv", self.data_array, delimiter=",")
                

        
    
    def clear_data(self):
        self.data_array =  np.array([])# reset data_array to empty np array
        
    def get_num_samples(self):
        return len(self.data_array)#the size of data_array
    
    def calc_sampling_rate(self):
           
        # dff = np.diff(self.data_array, n =1, axis =0)
        # mean = np.mean(dff, axis = 0)
        # print("mean[0]",mean[0])
        mean_diff = np.mean(np.diff(self.data_array[:,0],1,0))
        sampling_rate = 1000000/mean_diff
        print(sampling_rate)
        # return (1000000 / mean[0]) 
        return sampling_rate