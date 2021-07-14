import numpy as np

def trace(A):
 m = np.shape(A)[0]
 n = np.shape(A)[1]

 g = np.zeros((m,n))
 
 for i in range(m):
      for j in range(n):
          if (i==j):
                g+=A[i][j]
          else:
                 g+=0

    
 return g



