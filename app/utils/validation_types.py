from enum import Enum


class ValidationTypes(Enum):
    STRING = ("must be string.", "string")
    INTEGER = ("must be integer.", "integer")
    NOT_NULL = ("can't be null.", "not_null")
    OBJECT = ("must be an object.", "object")
    ARRAY_OBJECT = ("must be an array of objects.", "array_object")
    ARRAY_STRING = ("must be an array of strings.", "array_string")
    ARRAY_NUMBER = ("must be an array of numbers.", "array_number")

    def __init__(self, error_message, func_name=None):
        self.error_message = error_message
        self.func_name = func_name

    @property
    def msg(self):
        return self.error_message

    @property
    def foo(self):
        return self.func_name
