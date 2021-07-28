import numpy as np

def outer_product(F, G):

    b = np.size(F)
    r = np.size(G)
  

    W= np.zeros((b,r))

    for i in range(b):
        for j in range(r):
                W[i, j] = F[i] * G[j]
                

    return W
