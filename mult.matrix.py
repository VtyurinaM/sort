# -*- coding: utf-8 -*-
import numpy as np
n=3
A=np.zeros([n,n])
B=np.zeros([n,n])
C=np.zeros([n,n])
def ints(A):
    for i in range(0,len(A)):
        for j in range(0,len(A[i])):
            A[i][j]=np.random.randint(1,10)
    return A
def  mult(A,B,C):
    for i in range(0,n):
        for j in range(0,n):
            C[i][j]=0
            for k in range(0,n):
                C[i][j]=C[i][j]+A[i][k]*B[k][j]
    return C
A1=[[1,2,1],[1,2,1],[1,2,1]]
B1=[[1,2,2],[1,2,2],[1,2,2]]
ints(A)
ints(B)
print(A,B,mult(A,B,C),sep='\n\n')