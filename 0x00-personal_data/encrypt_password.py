#!/usr/bin/env python3
import bcrypt


def hash_password(password):
    """Hash the provided password using bcrypt

    Args:
        password (str): _description_

    Returns:
        Union[bytes, None]: _description_
    """
    # Generate a random salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password, password):
    """check if the password is hashed

    Args:
        hashed_password (bool): _description_
        password (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
