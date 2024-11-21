#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy.exc import InvalidRequestError, NoResultFound
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)  # Clear existing database
        Base.metadata.create_all(self._engine)  # Create new tables
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.
        Args:
            email (str): The user's email address.
            hashed_password (str): The hashed password of the user.
        Returns:
            User: The newly created User object.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()  # Commit to save changes to the database
        self._session.refresh(new_user)
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user in the database based on arbitrary keyword arguments.
        Args:
            kwargs: Arbitrary keyword arguments to filter the query.
        Returns:
            User: The first User object matching the query.
        Raises:
            NoResultFound: If no matching user is found.
            InvalidRequestError: If invalid query arguments are provided.
        """
        if not kwargs:
            raise InvalidRequestError("No arguments provided for query")

        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found with the specified criteria")
        except Exception as e:
            raise InvalidRequestError(f"Invalid query arguments: {e}")
