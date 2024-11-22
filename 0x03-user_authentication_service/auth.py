#!/usr/bin/env python3
"""
Auth module to handle user authentication and registration.
"""

from db import DB
from user import User
from bcrypt import hashpw, gensalt
from typing import Optional


def _hash_password(password: str) -> bytes:
    """Hash a password with bcrypt."""
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with the given email and password.
        Raises a ValueError if the user already exists.
        """
        try:
            # Check if user exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # User does not exist; proceed to create a new one
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password.decode('utf-8'))
            return new_user
