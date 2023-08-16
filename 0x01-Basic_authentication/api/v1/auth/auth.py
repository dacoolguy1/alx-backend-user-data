#!/usr/bin/env python3
"""flask authentication"""
from flask import request
from typing import List, TypeVar


class Auth():
    """flask authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
            path (str): _description_
            excluded_paths (List[str]): _description_

        Returns:
            bool: _description_
        """
        if (path is None):
            return True
        if (excluded_paths is None or len(excluded_paths) == 0):
            return True
        path_slash = path.endswith("/")
        for excluded_path in excluded_paths:
            if excluded_path.endswith("/"):
                excluded_path = excluded_path[:-1]

            if path_slash:
                if path == excluded_path:
                    return False
            else:
                if path == excluded_path or path + "/" == excluded_path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_

        Returns:
            _type_: _description_
        """
        return None
