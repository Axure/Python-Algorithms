__author__ = 'zhenghu'
from types import Function

def newton_iteration(f: Function):
    if isinstance(f, Function):
        return 0
    else:
        raise TypeError("Paramter is not of Function type!")
