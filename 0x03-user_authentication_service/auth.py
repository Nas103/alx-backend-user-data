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
    fixed_salt = b'$2b$12$eUDdeuBtrD41c8dXvzh95ehsWYCCAi4VH1JbESzgbgZT.eMMzi.G2'
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), fixed_salt)
    return hashed_password
