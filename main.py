from mat_mul import mat_mul
from pnorm import pnorm
from trace import trace
from transpose import transpose
from dot_product import dotp
import numpy as np

m = 5
n = 6
p = 3

A = np.arange(m*n).reshape(m, n)
B = np.arange(n*p).reshape(n, p)
D=np.arange(m).reshape(m, 1)
E=np.arange(n).reshape(n, 1)
trace_exact = np.trace(A)
C_exact = np.matmul(A, B)
C = mat_mul(A, B)

print('exact:\n', C_exact)
print('computed:\n', C)

n = 5
v = np.arange(-n, 0)
p = 3

norm = pnorm(v, p)
norm_exact = np.linalg.norm(v, p)

print('exact:\n', norm_exact)
print('computed:\n', norm)


trace = trace(A)
print(trace)
print(trace_exact)

transp = transpose(A)
print(transp)
print(A.T)

dot_product=dotp(v, p)
print(dot_product)
