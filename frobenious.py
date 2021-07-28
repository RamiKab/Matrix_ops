import numpy as np

def frobenious(A):
    m = np.shape(A)[0]
    n = np.shape(A)[1]
    total_squares=0.
    for i in range(m):
        for j in range(n):
            total_squares+=A[i][j]**2

    total_squares=np.sqrt(total_squares)
    return total_squares
    