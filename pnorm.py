import numpy as np

def pnorm(v, p):
    n = np.size(v)
    norm = 0.
    for i in range(n):
        norm += np.absolute(v[i] ** p)

    norm = norm ** (1/p)
    return norm