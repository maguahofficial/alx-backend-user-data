#!/usr/bin/env python3
"""
This The Main file
"""
from auth import Auth

emailx = 'bob@bob.com'
passwordx = 'MyPwdOfBob'
auth = Auth()

auth.register_user(emailx, passwordx)

print(auth.valid_login(emailx, passwordx))

print(auth.valid_login(emailx, "WrongPwd"))

print(auth.valid_login("unknown@email", passwordx))

