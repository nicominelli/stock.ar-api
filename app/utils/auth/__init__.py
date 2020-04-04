from datetime import datetime
from functools import wraps
from time import time

from flask import current_app as app
from flask import request
from jwt import InvalidSignatureError, ExpiredSignatureError
from jwt import encode, decode
from werkzeug.security import generate_password_hash, check_password_hash

from app.utils.auth.roles import Roles
from app.utils.error_handler import ErrorHandler

access_tokens = list()
refresh_tokens = list()
EXPIRE_SECONDS = 60 * 60  # 1 hour


def validate_role(role_allowed: Roles, required_name: str):
    role_required = Roles.get_from_name(required_name)
    if role_required is None:
        return False
    return role_required.weight <= role_allowed.weight


def hash_password(password):
    return generate_password_hash(password)


def validate_password(user, password):
    return check_password_hash(user.password, password)


def token_generate(data):
    expiration_time = time() + EXPIRE_SECONDS
    username = data.get('username') or data.username
    role = data.get('role') or data.role.name
    key = app.config['SECRET_KEY']
    a_payload = {'username': username, 'role': role, 'exp': expiration_time}
    access_token = encode(a_payload, key, algorithm='HS256').decode('utf-8')
    r_payload = {'access_token': access_token, 'exp': expiration_time}
    refresh_token = encode(r_payload, key, algorithm='HS256').decode('utf-8')
    access_tokens.append(access_token)
    refresh_tokens.append(refresh_token)
    expires = datetime.fromtimestamp(expiration_time).isoformat()
    data = {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'expires': expires
    }
    return data


def token_validate(token, refresh_token=False):
    key = app.config['SECRET_KEY']
    list_to_search = refresh_tokens if refresh_token else access_tokens
    if token in list_to_search:
        payload = decode(token, key, algorithms=['HS256'])
        return payload
    ErrorHandler.forbidden(msg="Invalid credentials.")


def token_invalidate(token):
    index = access_tokens.index(token)
    access_tokens.pop(index)
    refresh_tokens.pop(index)


def token_refresh(token):
    r_payload = token_validate(token, refresh_token=True)
    a_payload = token_validate(r_payload['access_token'])
    token_invalidate(r_payload['access_token'])
    return token_generate(a_payload)


def login_required(foo=None, role=Roles.USER):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if 'X-Auth-Token' in request.headers:
                token = request.headers['X-Auth-Token']
                try:
                    payload = token_validate(token)

                    allowed = validate_role(role, payload['role'])
                    if not allowed:
                        msg = "Invalid permissions for this action."
                        ErrorHandler.unauthorized(msg=msg)
                except InvalidSignatureError:
                    ErrorHandler.unauthorized(msg="Invalid credentials.")
                except ExpiredSignatureError:
                    ErrorHandler.unauthorized(msg="Token expired.")
            elif 'X-Caller-Role' in request.headers:
                if request.headers['X-Caller-Role'] != 'admin':
                    ErrorHandler.unauthorized(msg="Invalid credentials.")
            else:
                ErrorHandler.unauthorized(msg="Invalid credentials.")
            return f(*args, **kwargs)

        return wrapper

    if foo:
        return decorator(foo)
    return decorator
