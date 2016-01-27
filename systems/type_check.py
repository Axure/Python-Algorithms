from typing import *
import typing

def type_check(func):
    def func_wrapper(*args, **kwargs):
        print(typing.get_type_hints(func))

        arg_count = func.__code__.co_argcount
        arg_name_list = func.__code__.co_varnames[:arg_count]
        arg_name_with_type_dict = typing.get_type_hints(func)
        func_args_with_type = map(lambda x: ( (x, arg_name_with_type_dict[x]) ), arg_name_list)
        func_args_with_type_and_value = zip(func_args_with_type, args)

        # Type checking
        for index in range(arg_count):
            print(arg_name_list[index])
            expected_type = arg_name_with_type_dict[arg_name_list[index]]
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
        result = func(*args, **kwargs)
        if 'return' in arg_name_with_type_dict:
            expected_type = arg_name_with_type_dict['return']
            if not isinstance(result, expected_type):
                raise TypeError("Return type mismatch! Designated " + expected_type.__name__ + ", got " + type(result).__name__)
        else:
            if result is not None:
                raise TypeError("Return type mismatch! Designated None, got " + type(result).__name__)
        return result
    return func_wrapper
