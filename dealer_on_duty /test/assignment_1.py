def make_list(sequence: str) -> list:
    """
    Convert a comma-separated string into a list.

    Args:
        sequence (str): The input string containing elements separated by commas.

    Returns:
        list: A list containing the elements from the input string.
    """
    return sequence.split(',')


def make_tuple(sequence: str) -> tuple:
    """
    Convert a comma-separated string into a tuple.

    Args:
        sequence (str): The input string containing elements separated by commas.

    Returns:
        tuple: A tuple containing the elements from the input string.
    """
    return tuple(sequence.split(','))


if __name__ == '__main__':
    user_input = input('Enter a sequence of comma-separated numbers: like 34,67,55,33,12,98 - ')
    print(make_list(user_input))
    print(make_tuple(user_input))
