import importlib

from app.api import dto_module
from .error_codes import ErrorCode as Codes
from .error_handler import ErrorHandler as Handler
from .validation_types import ValidationTypes as VTypes


def validate(json, schema, method):
    possibles = "{}_POSSIBLES".format(method)
    if possibles in schema:
        invalids = validate_possibles(json, schema[possibles])
        if len(invalids) > 0:
            invalids = ", ".join(invalids)
            msg = "Following parameters aren't allowed: {}".format(invalids)
            Handler.bad_request(Codes.PARAM_NOT_ALLOWED, msg)
    if method in schema:
        validate_params(json, schema[method])
    class_ = getattr(importlib.import_module(dto_module), schema['DTO'])
    return class_(json)


def validate_params(json, schema):
    v = Validator()
    for key in schema:
        value = json.get(key)
        if isinstance(schema[key], tuple):
            f = getattr(v, schema[key][0].foo)
            f(key, value)
            if value:
                for i in value:
                    validate_params(i, schema[key][1])
        else:
            for validation in schema[key]:
                f = getattr(v, validation.foo)
                f(key, value)


def validate_possibles(json, possibles, parent=None):
    invalids = []
    for key in json:
        if key in possibles or "{}.{}".format(parent, key) in possibles:
            if isinstance(json[key], dict):
                new_parent = "{}.{}".format(parent, key) if parent else key
                inv = validate_possibles(json[key], possibles, new_parent)
                if len(inv) > 0:
                    invalids.extend(inv)
            elif isinstance(json[key], list):
                for i in json[key]:
                    pos = next(x for x in possibles if isinstance(x, list))
                    invalids.extend(validate_possibles(i, pos, key))
        else:
            if parent is not None:
                invalids.append("{}.{}".format(parent, key))
            else:
                invalids.append(key)
    return invalids


class Validator:
    @staticmethod
    def not_null(key, value):
        cond_1 = value is None
        cond_2 = isinstance(value, str) and len(value) == 0
        if cond_1 or cond_2:
            msg = "{} {}".format(key, VTypes.NOT_NULL.msg)
            Handler.bad_request(Codes.PARAM_CANT_BE_NULL, msg)

    @staticmethod
    def string(key, value):
        if value is not None:
            if not isinstance(value, str):
                msg = "{} {}".format(key, VTypes.STRING.msg)
                Handler.bad_request(Codes.PARAM_MUST_BE_STRING, msg)

    @staticmethod
    def integer(key, value):
        if value is not None:
            if not isinstance(value, int):
                msg = "{} {}".format(key, VTypes.INTEGER.msg)
                Handler.bad_request(Codes.PARAM_MUST_BE_INTEGER, msg)

    @staticmethod
    def object(key, value):
        if value is not None:
            if not isinstance(value, dict):
                msg = "{} {}".format(key, VTypes.OBJECT.msg)
                Handler.bad_request(Codes.PARAM_MUST_BE_OBJECT, msg)

    @staticmethod
    def array_object(key, value):
        if value is not None:
            if not isinstance(value, list):
                msg = "{} {}".format(key, VTypes.ARRAY_OBJECT.msg)
                Handler.bad_request(Codes.PARAM_MUST_BE_ARRAY_OBJECT, msg)
            else:
                for i in value:
                    if not isinstance(i, dict):
                        msg = "{} {}".format(key, VTypes.ARRAY_OBJECT.msg)
                        code = Codes.PARAM_MUST_BE_ARRAY_OBJECT
                        Handler.bad_request(code, msg)

    @staticmethod
    def array_string(key, value):
        if value is not None:
            if not isinstance(value, list):
                msg = "{} {}".format(key, VTypes.ARRAY_STRING.msg)
                Handler.bad_request(Codes.PARAM_MUST_BE_ARRAY_STRING, msg)
            else:
                for i in value:
                    if not isinstance(i, str):
                        msg = "{} {}".format(key, VTypes.ARRAY_STRING.msg)
                        code = Codes.PARAM_MUST_BE_ARRAY_STRING
                        Handler.bad_request(code, msg)

    @staticmethod
    def array_number(key, value):
        if value is not None:
            if not isinstance(value, list):
                msg = "{} {}".format(key, VTypes.ARRAY_NUMBER.msg)
                Handler.bad_request(Codes.PARAM_MUST_BE_ARRAY_NUMBER, msg)
            else:
                for i in value:
                    if not isinstance(i, int):
                        msg = "{} {}".format(key, VTypes.ARRAY_NUMBER.msg)
                        code = Codes.PARAM_MUST_BE_ARRAY_NUMBER
                        Handler.bad_request(code, msg)
