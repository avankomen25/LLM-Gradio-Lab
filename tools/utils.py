"""Shared utility helpers for all tool modules."""

import os


def is_path_safe(path):
    """Return True if *path* is safe to open, False otherwise.

    A path is considered unsafe if it is absolute or if any component
    of the path is ``..`` (directory traversal).

    >>> is_path_safe('tools/ls.py')
    True
    >>> is_path_safe('README.md')
    True
    >>> is_path_safe('/etc/passwd')
    False
    >>> is_path_safe('../secret.txt')
    False
    >>> is_path_safe('tools/../../secret.txt')
    False
    """
    if os.path.isabs(path):
        return False
    if '..' in path.replace('\\', '/').split('/'):
        return False
    return True
