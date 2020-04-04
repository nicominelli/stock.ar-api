import json
import unittest

import app
from app.utils.environment import Environment
from app.utils.error_codes import ErrorCode

# headers = {
#     'Accept': 'application/json',
#     'Content-Type': 'application/json'
# }
# admin_headers = {**headers, 'X-Caller-Role': 'admin'}
#
#
# def get_user():
#     user = {
#         'username': 'test_user',
#         'password': 'test_user',
#         'role_id': 1
#     }
#     return user
#
#
# class TestAuth(unittest.TestCase):
#     def setUp(self):
#         test_app = app.create_app(Environment.TESTING)
#         test_app.testing = True
#         self.app = test_app.test_client()
#
#     def test_login_ok(self):
#         # Create the user
#         url = '/auth/users'
#         user = get_user()
#         resp = self.app.post(url, headers=admin_headers, data=json.dumps(user))
#         self.assertEqual(resp.status_code, 201)
#         user_id = resp.json['id']
#         # Logs with the credentials
#         login_data = json.dumps({
#             'username': user['username'],
#             'password': user['password']
#         })
#         resp = self.app.post('/auth/login', headers=headers, data=login_data)
#         self.assertEqual(resp.status_code, 200)
#         # Deletion of the created resources
#         resp = self.app.delete('{}/{}'.format(url, user_id), headers=admin_headers)
#         self.assertEqual(resp.status_code, 200)
#
#     def test_login_nok(self):
#         # Create de user
#         url = '/auth/users'
#         user = get_user()
#         resp = self.app.post(url, headers=admin_headers, data=json.dumps(user))
#         self.assertEqual(resp.status_code, 201)
#         user_id = resp.json['id']
#         # Wrong password
#         login_data = json.dumps({
#             'username': user['username'],
#             'password': 'asd'
#         })
#         resp = self.app.post('/auth/login', headers=headers, data=login_data)
#         self.assertEqual(resp.status_code, 401)
#         cause = resp.json['cause']
#         self.assertEqual(cause['code'], ErrorCode.UNAUTHORIZED.code)
#         self.assertEqual(cause['description'], ErrorCode.UNAUTHORIZED.msg)
#         # Wrong username
#         login_data = json.dumps({
#             'username': 'asd',
#             'password': user['password']
#         })
#         resp = self.app.post('/auth/login', headers=headers, data=login_data)
#         self.assertEqual(resp.status_code, 403)
#         cause = resp.json['cause']
#         self.assertEqual(cause['code'], ErrorCode.FORBIDDEN.code)
#         self.assertEqual(cause['description'], ErrorCode.FORBIDDEN.msg)
#         # Delete user
#         resp = self.app.delete('{}/{}'.format(url, user_id), headers=admin_headers)
#         self.assertEqual(resp.status_code, 200)
#
#     def test_auth_and_login_ok(self):
#         # Create de user
#         url = '/auth/users'
#         user = get_user()
#         resp = self.app.post(url, headers=admin_headers, data=json.dumps(user))
#         self.assertEqual(resp.status_code, 201)
#         user_id = resp.json['id']
#         # Log de user
#         login_data = json.dumps({
#             'username': user['username'],
#             'password': user['password']
#         })
#         resp = self.app.post('/auth/login', headers=headers, data=login_data)
#         self.assertEqual(resp.status_code, 200)
#         access_token = resp.json['access_token']
#         auth_headers = {**headers, 'X-Auth-Token': access_token}
#         resp = self.app.get(url, headers=auth_headers)
#         self.assertEqual(resp.status_code, 200)
#         # Delete user
#         resp = self.app.delete('{}/{}'.format(url, user_id), headers=admin_headers)
#         self.assertEqual(resp.status_code, 200)
#
#     def test_logout_ok(self):
#         # Create the user
#         url = '/auth/users'
#         user = get_user()
#         resp = self.app.post(url, headers=admin_headers, data=json.dumps(user))
#         self.assertEqual(resp.status_code, 201)
#         user_id = resp.json['id']
#         # Login user
#         login_data = json.dumps({
#             'username': user['username'],
#             'password': user['password']
#         })
#         resp = self.app.post('/auth/login', headers=headers, data=login_data)
#         self.assertEqual(resp.status_code, 200)
#         access_token = resp.json['access_token']
#         # Logout de user
#         resp = self.app.post('/auth/logout', headers={**headers, 'X-Auth-Token': access_token})
#         self.assertEqual(resp.status_code, 204)
#         # Delete user
#         resp = self.app.delete('{}/{}'.format(url, user_id), headers=admin_headers)
#         self.assertEqual(resp.status_code, 200)
#
#     def test_refresh_ok(self):
#         url = '/auth/users'
#         user = get_user()
#         resp = self.app.post(url, headers=admin_headers, data=json.dumps(user))
#         self.assertEqual(resp.status_code, 201)
#         user_id = resp.json['id']
#         # Login user
#         login_data = json.dumps({
#             'username': user['username'],
#             'password': user['password']
#         })
#         resp = self.app.post('/auth/login', headers=headers, data=login_data)
#         self.assertEqual(resp.status_code, 200)
#         access_token = resp.json['access_token']
#         refresh_token = resp.json['refresh_token']
#         # Refresh user's tokens
#         auth_headers = {
#             **headers,
#             'X-Auth-Token': access_token,
#             'X-Refresh-Token': refresh_token
#         }
#         resp = self.app.post('/auth/refresh', headers=auth_headers)
#         self.assertEqual(resp.status_code, 200)
#         # Delete user
#         resp = self.app.delete('{}/{}'.format(url, user_id), headers=admin_headers)
#         self.assertEqual(resp.status_code, 200)
#
#     def test_refresh_nok(self):
#         url = '/auth/users'
#         user = get_user()
#         resp = self.app.post(url, headers=admin_headers, data=json.dumps(user))
#         self.assertEqual(resp.status_code, 201)
#         user_id = resp.json['id']
#         # Login user
#         login_data = json.dumps({
#             'username': user['username'],
#             'password': user['password']
#         })
#         resp = self.app.post('/auth/login', headers=headers, data=login_data)
#         self.assertEqual(resp.status_code, 200)
#         access_token = resp.json['access_token']
#         # Try to refresh user's tokens
#         resp = self.app.post('/auth/refresh', headers={
#             **headers,
#             'X-Auth-Token': access_token
#         })
#         self.assertEqual(resp.status_code, 403)
#         cause = resp.json['cause']
#         self.assertEqual(cause['code'], ErrorCode.FORBIDDEN.code)
#         self.assertEqual(cause['description'], ErrorCode.FORBIDDEN.msg)
#         # Delete user
#         resp = self.app.delete('{}/{}'.format(url, user_id), headers=admin_headers)
#         self.assertEqual(resp.status_code, 200)
#
#     def test_auth_nok(self):
#         # Request without credentials
#         users_url = '/auth/users'
#         roles_url = '/auth/roles'
#         resp = self.app.get(users_url, headers=headers)
#         self.assertEqual(resp.status_code, 401)
#         cause = resp.json['cause']
#         self.assertEqual(cause['code'], ErrorCode.UNAUTHORIZED.code)
#         self.assertEqual(cause['description'], ErrorCode.UNAUTHORIZED.msg)
#         # Request with forbidden role
#         resp = self.app.get(roles_url, headers=admin_headers)
#         role_user = next(i for i in resp.json if i['name'] == 'user')
#         user = json.dumps({
#             'username': 'test_user',
#             'password': 'test_user',
#             'role_id': role_user['id']
#         })
#         resp = self.app.post(users_url, headers=admin_headers, data=user)
#         self.assertEqual(resp.status_code, 201)
#         user_id = resp.json['id']
#         login_user = json.dumps({
#             'username': 'test_user',
#             'password': 'test_user'
#         })
#         resp = self.app.post('/auth/login', headers=headers, data=login_user)
#         self.assertEqual(resp.status_code, 200)
#         access_token = resp.json['access_token']
#         resp = self.app.post(users_url, headers={**headers, 'X-Auth-Token': access_token})
#         self.assertEqual(resp.status_code, 401)
#         resp = self.app.delete('{}/{}'.format(users_url, user_id), headers=admin_headers)
#         self.assertEqual(resp.status_code, 200)
#         # Non-existent auth token
#         resp = self.app.post(users_url, headers={**headers, 'X-Auth-Token': 'asd'})
#         self.assertEqual(resp.status_code, 403)
#         # Invalid admin token
#         resp = self.app.post(users_url, headers={**headers, 'X-Caller-Role': 'asd'})
#         self.assertEqual(resp.status_code, 401)
