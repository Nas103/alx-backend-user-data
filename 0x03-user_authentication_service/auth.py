import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with a fixed salt.

    Args:
        password (str): The password string to be hashed.

    Returns:
        bytes: The salted hash of the password.
    """
    # Using a fixed salt to generate the same output for testing
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
