# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:12:10 2019

@author: Vivek Chandrasekaran
"""

import numpy as np
from newton import Newton

class Rk_general:
    def __init__(self,A,b,c,h,obj):
        #initializing the values as per the Butcher table
        self.A=A
        self.b=b
        self.c=c
        self.h=h
        self.s=len(b.T)
        self.obj=obj

    
    def sol_imp(self,v0,x0,t):
        m=len(x0)
        ms=len(v0)
        e=np.ones(self.s)
        Gv=lambda v:v-np.kron(e,x0)-self.h*np.matmul(np.kron(self.A,np.eye((m))),self.obj.fun(v0,t))
        DGv=lambda v:np.eye((ms))-self.h*np.matmul(np.kron(self.A,np.eye((m))),self.obj.diff(v,t))
        #call Newton solver to solve for system of slopes
        v=Newton(Gv,DGv,1e-5,30,v0)
        #evaluate the next X value
        xnext=x0+self.h*np.matmul(np.kron(np.matmul(self.b,np.linalg.inv(self.A)),np.eye((m))),v-np.kron(e,x0))
        return xnext
        
    def sol_exp(self,x0,t):
        x=x0
        k=np.zeros((len(x0),len(self.b.T)))
        inter2=0
        for i in range (0,len(self.b.T)):
            inter=0
            for j in range(0,i):
                inter=inter+self.A[i,j]*k[:,j]
                x=x+self.h*sum
            t=t+self.c[i]*self.h
            k[:,i]=self.obj.fun(x,t)
            inter2=inter2+self.h*self.b[i]*k[i]
        xnext=x0+inter2
        return xnext
            
    
    
    



    