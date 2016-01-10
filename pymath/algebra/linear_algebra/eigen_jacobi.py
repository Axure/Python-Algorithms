from sympy import *
from numpy import *
from numpy import linalg as LA


def eigen_jacobi(A: matrix, p, q):
    B = A
    n = A.ndim
    if p > n or q > n or p == q:
        return
    if (A[p, q] == 0):
        return
    t1 = (A[q, q] - A[p, p]) / (2 * A[p, q])
    t = 1 / (absolute(t1) + sqrt(1 + t1 * t1))
    if t1 < 0 or (t == 0 and A[p, q] < 0):
        t = -t
    c = 1 / sqrt(1 + t * t)
    s = t * c
    b1 = A[p, :]
    b2 = A[q, :]
    b3 = c * b1 - s * b2
    b4 = s * b1 + c * b2
    B[p, :] = b3
    B[:, p] = transpose(b3)
    B[q, :] = b4
    B[:, q] = transpose(b4)
    B[p, p] = c * c * A[p, p] - 2 * s * c * A[p, q] + s * s * A[q, q]
    B[q, q] = s * s * A[p, p] + 2 * s * c * A[p, q] + c * c * A[q, q]
    B[p, q] = 0
    B[q, p] = 0
    return B


if __name__ == '__main__':
    print(3)
    A = matrix('[1 2 3; 2 5 6; 3 6 9]')
    print(eigen_jacobi(A, 1, 2))
