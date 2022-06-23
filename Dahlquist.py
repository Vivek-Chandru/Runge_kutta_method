# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 07:16:50 2019

@author: Vivek Chandrasekaran
"""
import numpy as np
class Dahlquist:

    def __init__(self,alpha):
        self.alpha = alpha
        
    def fun(self,x,t):
        return self.alpha*x
    
    def diff(self,x,t):
        return self.alpha*np.eye((len(x)))
    