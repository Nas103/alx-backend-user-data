#!/usr/bin/env python3
"""
Module for filtering log messages.
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes the password with a salt using bcrypt.
    Returns the hashed password as bytes.
    """
    salt = bcrypt.gensalt()  # Generates a salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates the provided password against the hashed password using bcrypt.
    Returns True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
