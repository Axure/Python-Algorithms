__author__ = 'zhenghu'

class InvalidParamterException(Exception):
    def __init__(self, name):
        Exception.__init__(self, name)

class UninitializedException(Exception):
    def __init__(self, name):
        Exception.__init__(self, name)
