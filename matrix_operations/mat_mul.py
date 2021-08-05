import numpy as np

def mat_mul(A, B):

    m = np.shape(A)[0]
    n = np.shape(A)[1]
    p = np.shape(B)[1]

    C = np.zeros((m,p))

    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]
                # C[i, j] = C[i, j] + A[i, k] * B[k, j]

    return C
