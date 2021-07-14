import numpy as np

def trace(A):
      m = np.shape(A)[0]
      n = np.shape(A)[1]

      p = min(m, n)

      trace = 0.

      for i in range(p):
            trace += A[i][i]
      
      return trace



