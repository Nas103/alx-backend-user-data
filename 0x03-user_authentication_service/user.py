#!/usr/bin/env python3
"""
User model definition using SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy User model for the 'users' table.
    
    Attributes:
        id (int): Primary key of the user.
        email (str): Non-nullable email of the user.
        hashed_password (str): Non-nullable hashed password of the user.
        session_id (str): Nullable session ID of the user.
        reset_token (str): Nullable reset token for password recovery.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
