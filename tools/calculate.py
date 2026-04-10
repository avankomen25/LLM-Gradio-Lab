"""Tool: evaluate a mathematical expression and return the result as JSON."""

import json


def calculate(expression):
    """Evaluate *expression* as a Python arithmetic expression.

    Returns a JSON string with key ``"result"`` on success, or key
    ``"error"`` if the expression cannot be evaluated.

    >>> calculate('2 + 2')
    '{"result": 4}'
    >>> calculate('10 * 3.5')
    '{"result": 35.0}'
    >>> calculate('not_a_number')
    '{"error": "Invalid expression"}'
    """
    try:
        result = eval(expression)  # noqa: S307
        return json.dumps({"result": result})
    except Exception:
        return json.dumps({"error": "Invalid expression"})


tool_schema = {
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Evaluate a mathematical expression",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to evaluate",
                }
            },
            "required": ["expression"],
        },
    },
}
