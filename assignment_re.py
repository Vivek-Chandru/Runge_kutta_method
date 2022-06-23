# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 20:12:21 2019

@author: Vivek Chandrasekaran
"""
import numpy as np
import math as m
from Dahlquist import Dahlquist
import matplotlib.pyplot as plt
from Rk_general import Rk_general


#time stepping function
obj=Dahlquist(10)
x0=np.array([1,20,30])
h=0.001


#""" uncomment for implicit Euler
# A=np.array([[1]])
# b=np.array([1])
# c=np.array([1])
# euler_imp=Rk_general(A,b,c,h,obj)

#uncomment to solve euler explicit
A=np.array([[0]])
b=np.array([1])
c=np.array([0])
euler_exp=Rk_general(A,b,c,h,obj)



#creating an object of the problem
time=10
n=int(time/h)
x=np.zeros((n,len(x0)))
x[0,:]=x0
error=np.zeros(n)
e=np.ones(len(b.T))
t=0;
v0=np.ones(len(x0)*len(b.T),'f')

# uncomment to solve implicit 
# for i in range(0,n-1):
#     x[i+1,:]=euler_imp.sol_imp(v0,x0,t)
#     v0=np.kron(x0,e)
#     x0=x[i+1,:]
#     error[i+1]=np.linalg.norm(x[i+1,:]-x[i,:])/np.linalg.norm(x[i,:])
#     t=t+h

# uncomment to solve explicit
for i in range(0,n-1):
    x[i+1,:]=euler_exp.sol_exp(x0,t)
    x0=x[i+1,:]
    error[i+1]=np.linalg.norm(x[i+1,:]-x[i,:])/np.linalg.norm(x[i,:])
    t=t+h

t=0
sol=np.zeros((n,1))
for i in range(0,n-1):
    sol[i+1,:]=m.exp(t)
    t=t+h
    

#plotting
f=plt.figure(1)
plt.plot(x[:,0])
plt.ylabel('Numerical solution')
plt.xlabel('Iterations')
f.show()

g=plt.figure(2)
plt.plot(error[:])
plt.xlabel('Iterations')
plt.ylabel('error')
g.show()