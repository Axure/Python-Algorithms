__author__ = 'zhenghu'
from .Exceptions import *


class ExtendedReals:
    # type = 0

    def __init__(self, a):
        # print("Intializing")
        if isinstance(a, float) or isinstance(a, int):
            # print("Intializing: case 2")
            self.type = 2
            self.value = a
        else:
            if isinstance(a, str):
                # print("Intializing: case 3")
                if a == 'p_i':
                    self.type = 3;
                else:
                    if a == 'n_i':
                        # print("Intializing: case 1")
                        self.type = 1;
                    else:
                        raise InvalidParamterException('Invalid constructor string!')

    def __eq__(self, other):
        if isinstance(other, ExtendedReals):
            return self.type == other.type and (self.type != 2 or self.value == other.value)
        else:
            return self.__eq__(ExtendedReals(other))

    def __str__(self):
        # print(self.type)
        if self.type == 2:
            # print("Printing: case 2: " + str(self.value))
            return str(self.value)
        else:
            if self.type == 1:
                # print("Printing: case 1: " + "-inf")
                return "-inf"
            else:
                if self.type == 3:
                    # print("Printing: case 3: " + "+inf")
                    return "+inf"
                else:
                    raise UninitializedException("The extended real number has not yet been intialized!")


class Interval:
    def __init__(self, lower: ExtendedReals, upper: ExtendedReals):
        if not isinstance(lower, ExtendedReals):
            try:
                self.lower = ExtendedReals(lower)
            except InvalidParamterException:
                raise TypeError("Lower bound cannot be converted to an extended real number!")
        else:
            self.lower = lower

        if not isinstance(upper, ExtendedReals):
            try:
                self.upper = ExtendedReals(upper)
            except InvalidParamterException:
                raise TypeError("Upper bound cannot be converted to an extended real number!")
        else:
            self.upper = upper

    def __str__(self):
        return "[" + str(self.lower) + ", " + str(self.upper) + "]"


class ExtendedRealLine(Interval):
    def __init__(self):
        Interval.__init__(self, 'n_i', 'p_i')


EXTENDED_REAL_LINE = ExtendedRealLine()

if __name__ == '__main__':
    print(3)
