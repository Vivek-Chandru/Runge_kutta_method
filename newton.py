# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:36:52 2019

@author: Vivek Chandrasekaran
"""
import numpy as np

#Newton Solver
def Newton(f,Df,tol,maxiter,x0):
    x=x0
    xold=x0
    i=1
    err=np.linalg.norm(x0)
    while ((err>=tol)&(i<maxiter)):
            x=xold - np.linalg.solve(Df(xold),f(xold))
            err=np.linalg.norm(x-xold)/np.linalg.norm(x)
            xold=x    
    return x
