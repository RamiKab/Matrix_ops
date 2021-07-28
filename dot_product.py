import numpy as np

def dotp(D, E):
    m= np.size(D)
    t = np.size(E)
    dot_product=0.
    for i in range(m):
         dot_product+=D[i]*E[i]

    return dot_product

