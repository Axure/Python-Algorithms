from sympy import *
from numpy import *
from numpy import linalg as LA

# Use sympy for matrix calculation?
if __name__ == 'main':
    print('haha')

    # Where are the adapters for the MacBook Pro

a = matrix('1 2 ; 3 4')  # let a be a matrix.

b = LA.eig(a)  # The eigenvalue of a. How to prettify it?
print(b)

c = a.itemsize
print(c)

d = a.ndim
print(d)

a = matrix('1 2 3; 4 5 6; 7 8 9')

d = a.size
print(d)
print(a[1, 1])
print(a[1, :])
print(a[:, 1])

print(a[1, :] * a[:, 1])
print(a[:, 1] * a[1, :])

array_1 = array((1, 2, 3))
array_2 = array((1, 2, 3))
array_3 = array((1, 2, 3))
matrix_1 = column_stack((array_1, array_2, array_3))
print(matrix_1)

help()
