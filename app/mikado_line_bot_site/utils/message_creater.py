"""This module is a script to create a message for tests.
"""

def create_single_text_message(message):
    """test method.

    Args:
        message (_type_): _description_

    Returns:
        _type_: _description_
    """
    if message == 'ありがとう':
        message = 'どういたしまして！'
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message
