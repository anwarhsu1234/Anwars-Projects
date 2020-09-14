# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:22:14 2020

@author: Anwar
"""
import glob
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture as GMM
from scipy.stats import pearsonr

class ML:
    
    def __init__(self):
        return         
        
    def train_hr_model(self,directory):
        all_files = glob.glob(directory)
        self.unique_ids = []

        fs = 50
      
        for index in range(len(all_files)):
            ind_file = (all_files[index].split("\\"))
            split = ind_file[-1].split("_")
            if split[0] not in self.unique_ids: 
                self.unique_ids.append(split[0])
    

        self.list_data = []
        self.list_sub = []
        self.list_ref = []

    
        for sub_id in self.unique_ids: 
    
            sub_files  = glob.glob(r'C:\Users\Anwar\Documents\ECE16\ece16-wi2020-anwarhsu\Lab-code\src\Python\directory\traning_set\%s?*.csv' % sub_id)
    
            for file in sub_files:
                temp_file = (file.split("\\") )
        
                data_array = np.genfromtxt(file, delimiter=',')
        
                HR = data_array[:,4] #get the ppg signal from data using slicing
                HR = HR[0:500]
                t = (data_array[:,0] - data_array[0,0])/1e6 #have time start at 0 and in seconds
                t = t[0:500]
                #preprocess your hr_data:removing baseline, smooth your signal using a low pass filter and normalize. 
                
                s_diff = np.diff(-HR,1,0)
                s_diff = np.append(s_diff, 0) 
        
        
                fc = 5  # Cut-off frequency of the filter
                w = fc / (fs / 2) # Normalize the frequency
                b, a = signal.butter(5, w, 'low')
                output = signal.filtfilt(b, a, s_diff)
       
                norm_signal = (output - np.min(output))/(np.max(output)-np.min(output)) #normalize signal
        
                self.list_data.append(norm_signal)#append the preprocessed data to list_data
                self.list_sub.append(sub_id) #append the subject id to list_sub
        
                #retrieve the reference heart rate from the filename.
                hr_file = file.split("\\")
                hr_file = hr_file[-1].split("_")
                hr_file = hr_file[-1].split(".")
                reference_HR = hr_file[0]
        
                #append the reference heart rate to list_ref
                self.list_ref.append(int(reference_HR))



        """train_data = np.empty(0)#make empty numpy array of size 0

        hold_out_data = np.empty(0)#make empty numpy array of size 0

        self.list_data = np.array(self.list_data)

        hold_out_subject = self.list_sub[0] #for now we’ll hold out the first training subject
        for ind, sub_id in enumerate(self.list_sub, start = 0):#enumerate the list_sub starting at 0. Look up enumerate function
  
            if(sub_id != hold_out_subject):#sub_id is not the same as hold_out_subject) 
                if(train_data.shape[0] == 0):
                    train_data = self.list_data[ind]
                else:
                    train_data = np.vstack((train_data,self.list_data[ind]))#concatenate numpy array train_data with the list_data at ind
    
            else:
                if(hold_out_data.shape[0] == 0):
                    hold_out_data = self.list_data[ind]  
                else:
                    hold_out_data = np.vstack((hold_out_data,self.list_data[ind]))#concatenate numpy array hold_out_data with list_data at ind
                    
        self.gmm_data = np.empty(0)

        for i in range(0,10):


            gmm = GMM(n_components = 2).fit(train_data.reshape(-1,1))        
            test_pred = gmm.predict(hold_out_data[i].reshape(-1,1))
    
    
            plt.subplot(5,2,i+1)
            plt.plot(test_pred)
            plt.plot(hold_out_data[i])
    
    
            if (self.gmm_data.shape[0] == 0):
                self.gmm_data = np.array(test_pred)
            else:
                self.gmm_data = np.vstack((self.gmm_data,np.array(test_pred)))"""


    def calc_hr(self):
        self.heartrate = []

        state = 0
        for i in self.gmm_data:
            count = 0

            for j in i:
                if j == 1 and state == 0:
                    count += 1
                    state = 1
                if state == 1 and j == 0:
                    state = 0
            self.heartrate.append((count -1) * 6)
    
        print("cacluated" ,self.heartrate)
        print("reference" ,self.list_ref2[0:10])
        
        
    def test_hr_model(self,directory):
        all_files = glob.glob(directory)
        self.unique_ids2 = []

        fs = 50
      
        for index in range(len(all_files)):
            ind_file = (all_files[index].split("\\"))
            split = ind_file[-1].split("_")
            if split[0] not in self.unique_ids2: 
                self.unique_ids2.append(split[0])
    

        self.list_data2 = []
        self.list_sub2 = []
        self.list_ref2 = []
        
        for sub_id in self.unique_ids2: 
    
            sub_files  = glob.glob(r'C:\Users\Anwar\Documents\ECE16\ece16-wi2020-anwarhsu\Lab-code\src\Python\directory\Test_set\%s?*.csv' % sub_id)
            for file in sub_files:
                temp_file = (file.split("\\") )
        
                data_array = np.genfromtxt(file, delimiter=',')
        
                HR = data_array[:,4] #get the ppg signal from data using slicing
                HR = HR[0:500]
                t = (data_array[:,0] - data_array[0,0])/1e6 #have time start at 0 and in seconds
                t = t[0:500]
                #preprocess your hr_data:removing baseline, smooth your signal using a low pass filter and normalize. 
                
                s_diff = np.diff(-HR,1,0)
                s_diff = np.append(s_diff, 0) 
        
        
                fc = 5  # Cut-off frequency of the filter
                w = fc / (fs / 2) # Normalize the frequency
                b, a = signal.butter(5, w, 'low')
                output = signal.filtfilt(b, a, s_diff)
       
                norm_signal = (output - np.min(output))/(np.max(output)-np.min(output)) #normalize signal
        
                self.list_data2.append(norm_signal)#append the preprocessed data to list_data
                self.list_sub2.append(sub_id) #append the subject id to list_sub
        
                #retrieve the reference heart rate from the filename.
                hr_file = file.split("\\")
                hr_file = hr_file[-1].split("_")
                hr_file = hr_file[-1].split(".")
                reference_HR = hr_file[0]
        
                #append the reference heart rate to list_ref
                self.list_ref2.append(int(reference_HR))
                
        self.train_data = np.empty(0)#make empty numpy array of size 0

        self.hold_out_data = np.empty(0)#make empty numpy array of size 0

        self.list_data = np.array(self.list_data)

        hold_out_subject = self.list_sub2[0] #for now we’ll hold out the first training subject
        for ind, sub_id in enumerate(self.list_sub, start = 0):#enumerate the list_sub starting at 0. Look up enumerate function
  
            
            if(self.train_data.shape[0] == 0):
               self.train_data = self.list_data[ind]
            else:
                self.train_data = np.vstack((self.train_data,self.list_data[ind]))#concatenate numpy array train_data with the list_data at ind
    
          
        for ind, sub_id2 in enumerate(self.list_sub2, start = 0):#enumerate the list_sub starting at 0. Look up enumerate function
  
            
            if(self.hold_out_data.shape[0] == 0):
               self.hold_out_data = self.list_data2[ind]
            else:
                self.hold_out_data = np.vstack((self.hold_out_data,self.list_data2[ind]))#c  
        
        
        
        self.gmm_data = np.empty(0)

        for i in range(0,10):

            
            gmm = GMM(n_components = 2).fit(self.train_data.reshape(-1,1))        
            test_pred = gmm.predict(self.hold_out_data[i].reshape(-1,1))
    
    
            plt.subplot(5,2,i+1)
            plt.plot(test_pred)
            plt.plot(self.hold_out_data[i])
    
    
            if (self.gmm_data.shape[0] == 0):
                self.gmm_data = np.array(test_pred)
            else:
                self.gmm_data = np.vstack((self.gmm_data,np.array(test_pred)))
                
        
                
                
         

        