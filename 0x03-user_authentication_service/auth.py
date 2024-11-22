#!/usr/bin/env python3
"""
Auth module for user authentication.
"""

import bcrypt
import uuid
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hash a password with bcrypt."""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """
        Register a user with an email and password.

        Args:
            email (str): User's email.
            password (str): User's password.

        Returns:
            User: The registered user object.

        Raises:
            ValueError: If a user with the email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except Exception:
            hashed_password = self._hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login credentials.

        Args:
            email (str): User's email.
            password (str): User's password.

        Returns:
            bool: True if login is valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except Exception:
            return False

    def _generate_uuid(self) -> str:
        """
        Generate a new UUID.

        Returns:
            str: A string representation of a new UUID.
        """
        return str(uuid.uuid4())

    def create_session(self, email: str) -> str | None:
        """
        Create a session for a user and return the session ID.

        Args:
            email (str): User's email.

        Returns:
            str: Session ID if user exists, None otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = self._generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None
