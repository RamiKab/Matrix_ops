from matrix_operations.mat_mul import mat_mul
from matrix_operations.pnorm import pnorm
from matrix_operations.trace import trace
from matrix_operations.transpose import transpose
from matrix_operations.dot_product import dotp
from matrix_operations.determinant import determinant_3x3, determinant_4x4
from matrix_operations.outer_product import outer_product
from matrix_operations.frobenius import frobenius
import numpy as np

m = 6
n = 5
p = 3
t=m
b=4
r=7
A = np.arange(m*n).reshape(m, n)
B = np.arange(n*p).reshape(n, p)
# J = np.arange(3*3).reshape(3, 3)
J = np.identity(3)
# J4 = np.arange(4*4).reshape(4, 4)
J4 = np.identity(4)
D=np.arange(m)
E=np.arange(t)
F=np.arange(b)
G=np.arange(r)
trace_exact = np.trace(A)

C_exact = np.dot(A, B)
C = mat_mul(A, B)

print('exact:\n', C_exact)
print('computed:\n', C)

n = 5
v = np.arange(-n, 0)
p = 2

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

dot_product=dotp(D, E)
print(dot_product)
dotproductExact=np.dot(D,E)
print(dotproductExact)

outer_calc=outer_product(F,G)
print(outer_calc)
outer_exact=np.outer(F,G)
print(outer_exact)


f_norm=frobenius(A)
print(f_norm)
f_exact=np.linalg.norm(A)
print(f_exact)

determinant_3 = determinant_3x3(J)
print(determinant_3)
determinant3_exact = np.linalg.det(J)
print(determinant3_exact)

determinant_4=determinant_4x4(J4)
print(determinant_4)
determinant4_exact=np.linalg.det(J4)
print(determinant4_exact)