import numpy as np

def transpose(A):
  m = np.shape(A)[0]
  n = np.shape(A)[1]

  transp = np.zeros((n, m)) 
  for i in range(m):
    for j in range(n):
        transp[j][i] = A[i][j]

  return transp