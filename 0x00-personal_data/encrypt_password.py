#!/usr/bin/env python3
"""
    Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Function returns a salted,hashed password and which is a byte string """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Function validates provided password matches the hashed password """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
