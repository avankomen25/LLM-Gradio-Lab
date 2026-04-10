"""Tool: read and return the full text contents of a file."""

from tools.utils import is_path_safe


tool_schema = {
    "type": "function",
    "function": {
        "name": "cat",
        "description": (
            "Read and return the full contents of a file. "
            "Use this whenever the user asks to see, read, open, or display a file."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "description": "The path to the file to read",
                }
            },
            "required": ["file"],
        },
    },
}


def cat(file):
    """Return the full text contents of *file*.

    Blocks absolute paths and directory traversal.  Returns a plain
    error string (not an exception) on failure so the LLM can relay
    the message to the user.

    >>> cat('tools/cat.py').startswith('\"\"\"Tool: read')
    True
    >>> cat('nonexistent_file.txt')
    "Error: file 'nonexistent_file.txt' not found"
    >>> cat('/etc/passwd')
    "Error: path '/etc/passwd' is not allowed"
    >>> cat('../secret.txt')
    "Error: path '../secret.txt' is not allowed"
    >>> import unittest.mock
    >>> with unittest.mock.patch('builtins.open', side_effect=UnicodeDecodeError('utf-8', b'', 0, 1, 'bad')):
    ...     cat('tools/cat.py')
    "Error: file 'tools/cat.py' is not a text file"
    """
    if not is_path_safe(file):
        return f"Error: path '{file}' is not allowed"
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: file '{file}' not found"
    except UnicodeDecodeError:
        return f"Error: file '{file}' is not a text file"
