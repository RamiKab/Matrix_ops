import numpy as np

def determinant_2x2(A):
    return A[0,0] * A[1,1] - A[0,1] * A[1,0]

def determinant_3x3(A):
    det = 0.
    det += A[0][0] * determinant_2x2(A[1:, 1:])
    det -= A[0][1] * determinant_2x2(A[1:2,0::2 ])
    det += A[0][2] * determinant_2x2(A[1:2,0:2 ])

    return det

def determinant_4x4(A):
    det = 0.
    det += A[0][0] * determinant_3x3(A[1:, 1:])
    det -= A[0][1] * determinant_3x3(A[1:, 1:3])
    det += A[0][2] * determinant_3x3(A[1:,0:2 ])
    det -= A[0][3] * determinant_3x3(A[1:,0:3])

    return det
