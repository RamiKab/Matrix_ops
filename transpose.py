import numpy as np

def transpose(A):
 m = np.shape(A)[0]
 n = np.shape(A)[1]

 result=0 
 for i in range(len(A)):
   
   for j in range(len(A[0])):
       result[j][i] = A[i][j]


 return result