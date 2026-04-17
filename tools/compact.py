"""Tool: summarize the current conversation history into 1-5 lines using a Chat subagent."""


def compact(messages, subagent):
    """Summarize *messages* into 1-5 lines of plain text using a Chat *subagent*.

    *subagent* must be an object with a ``send_message(text)`` method — in
    production this is a ``Chat`` instance; in tests it is a mock.  The caller
    is responsible for creating the subagent, which keeps this function simple
    and avoids any circular-import concerns.

    Only user and assistant turns are included in the prompt sent to the subagent:

    >>> import unittest.mock
    >>> mock_subagent = unittest.mock.MagicMock()
    >>> mock_subagent.send_message.return_value = 'User asked what 2+2 is. The answer is 4.'
    >>> result = compact(
    ...     [
    ...         {'role': 'system', 'content': 'Talk like a pirate.'},
    ...         {'role': 'user', 'content': 'what is 2+2?'},
    ...         {'role': 'assistant', 'content': 'Arrr, it be 4!'},
    ...     ],
    ...     mock_subagent,
    ... )
    >>> result
    'User asked what 2+2 is. The answer is 4.'

    >>> call_args = mock_subagent.send_message.call_args[0][0]
    >>> 'USER: what is 2+2?' in call_args
    True
    >>> 'ASSISTANT: Arrr, it be 4!' in call_args
    True
    >>> 'system' not in call_args
    True
    """
    conversation_lines = []
    for m in messages:
        if m['role'] in ('user', 'assistant') and m.get('content'):
            conversation_lines.append(f"{m['role'].upper()}: {m['content']}")
    conversation_text = '\n'.join(conversation_lines)

    return subagent.send_message(
        "Summarize this conversation in 1-5 lines of plain text, "
        "capturing only the key facts and context needed to continue it. "
        "Do NOT use pirate speak — write plain, clear prose:\n\n"
        + conversation_text
    )
