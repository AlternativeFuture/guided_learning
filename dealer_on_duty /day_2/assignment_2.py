def is_palindrome(text: str) -> bool:
    """
    Check if the input text is a palindrome.

    Args:
        text (str): The input text to be checked for palindromic.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    return text == text[::-1]


if __name__ == '__main__':
    print(is_palindrome('racecar'))
    print(is_palindrome('level'))
    print(is_palindrome('reverse'))
