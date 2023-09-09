def count_characters(text: str) -> dict:
    """
    Count the frequency of each character in the input text.

    Args:
        text (str): The input text in which character frequencies will be counted.

    Returns:
        dict: A dictionary where keys are characters and values are the frequency of each character.
    """
    char_frequency = {}

    for char in text:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    return char_frequency


if __name__ == '__main__':
    print(count_characters('google.com'))
    print(count_characters('aabbccddggzzvvxx'))
