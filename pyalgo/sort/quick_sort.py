from typing import *
import typing
from pyalgo.sort import selection_sort

def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        print(typing.get_type_hints(func))

        arg_count = func.__code__.co_argcount
        arg_name_list = func.__code__.co_varnames[:arg_count]
        arg_name_with_type_list = typing.get_type_hints(func)
        func_args_with_type = map(lambda x: ( (x, arg_name_with_type_list[x]) ), arg_name_list)
        func_args_with_type_and_value = zip(func_args_with_type, args)

        ### Type checking
        for index in range(arg_count):
            print(arg_name_list[index])
            expected_type = arg_name_with_type_list[arg_name_list[index]]
            if not isinstance(args[index], expected_type):
                raise TypeError("Type mismatch! Expected: '" + expected_type.__name__ + "'. Given: '" + type(args[index]).__name__ + "'.")

        print("Function varaible names", func.__code__.co_varnames)
        print("Function varaibles with type")
        for haha in func_args_with_type_and_value:
            print(haha)
        print("Function name", func.__name__)
        print("Passed args name", args)
        for param_name, param_type in typing.get_type_hints(func).items():
            print(param_name, param_type)
        for arg in args:
            print(arg)
        # return "<p>{0}</p>".format(func(args))
        return func(*args, **kwargs)
    return func_wrapper

@p_decorate
def quick_sort(a: list):
    j = 3
    for i in a:
        print(i)
    return a

@p_decorate
def median_of_three(za: list, l: int, r: int) -> int:
    print(za, l, r)
    return za



if __name__ == '__main__':
    # print(3)
    # quick_sort([3, 4, 5])
    median_of_three(3, 4, 5)

    print(quick_sort([3, 4, 5]))
    # print(typing.get_type_hints(quick_sort))
    # print(typing.get_type_hints(median_of_three))
