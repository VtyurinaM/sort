# -*- coding: utf-8 -*-
import numpy as np
from random import randint
n=7
A=np.zeros(n)
for i in range(0,n):
    A[i]=randint(1,100)
print(A,'\n')
for i in range(0,n-1):
    for j in range(0,n-1-i):
        if A[j+1]<A[j]:
            t=A[j]
            A[j]=A[j+1]
            A[j+1]=t
            print(A)
print(A,'\n')
        