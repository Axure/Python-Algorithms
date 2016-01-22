from typing import *
import typing
from pyalgo.sort import selection_sort
from typings import type_check


@type_check
def quick_sort(a: list) -> list:
    j = 3
    for i in a:
        print(i)
    return a

@type_check
def median_of_three(za: list, l: int, r: int) -> list:
    print(za, l, r)
    return za



if __name__ == '__main__':
    # print(3)
    # quick_sort([3, 4, 5])
    median_of_three([3, 4], 4, 5)

    print(quick_sort([3, 4, 5]))
    # print(typing.get_type_hints(quick_sort))
    # print(typing.get_type_hints(median_of_three))
