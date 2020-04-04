import enum


class ErrorCode(enum.Enum):
    GENERIC_ERROR = (1, "Generic error.")
    UNAUTHORIZED = (2, "Unauthorized.")
    FORBIDDEN = (3, "Forbidden.")
    PAGE_NOT_FOUND = (4, "Page Not Found.")
    NOT_ALLOWED = (5, "Method Not Allowed.")
    INTERNAL_SERVER_ERROR = (6, "Internal Server Error.")
    RESOURCE_NOT_FOUND = (10, "Resource not found.")
    RESOURCE_FOUND = (11, "Resource already exists.")
    PARAM_CANT_BE_NULL = (20, "Parameter can't be null.")
    PARAM_MUST_BE_STRING = (21, "Parameter must be string.")
    PARAM_NOT_ALLOWED = (22, "Parameters not allowed.")
    PARAM_MUST_BE_INTEGER = (23, "Parameter must be integer.")
    PARAM_MUST_BE_OBJECT = (24, "Parameter must be an object.")
    PARAM_MUST_BE_ARRAY_OBJECT = (25, "Parameter must be an array of objects.")
    PARAM_MUST_BE_ARRAY_STRING = (25, "Parameter must be an array of strings.")
    PARAM_MUST_BE_ARRAY_NUMBER = (25, "Parameter must be an array of numbers.")

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
