def reverse_string(text: str) -> str:
    """
        Reverse the characters in the input text.

        Args:
            text (str): The input text to be reversed.

        Returns:
            str: The reversed text.
        """
    return text[::-1]


if __name__ == '__main__':
    user_input = input('Enter a string for reversal. ')
    print(reverse_string(user_input))
