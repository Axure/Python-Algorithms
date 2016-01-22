__author__ = 'zhenghu'
from pymath.types import Function
import sympy

def newton_iteration(f: Function):
    if isinstance(f, Function):
        return 0
    else:
        raise TypeError("Paramter is not of Function type!")


if __name__ == '__main__':
    print(3)
