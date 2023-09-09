def generate_square_dict(number: int) -> dict:
    """
    Generate a dictionary of squares for numbers from 1 to the given 'number'.

    Args:
        number (int): The maximum number for which squares will be calculated.

    Returns:
        dict: A dictionary where keys are numbers from 1 to 'number' and values are their squares.
    """
    square_dict = {}

    for n in range(1, number + 1):
        square_dict[n] = n * n

    return square_dict


if __name__ == "__main__":
    user_input = input("Enter a number. ")
    if user_input.isdigit():
        print(generate_square_dict(int(user_input)))
    else:
        print('Invalid input! You should enter a number!')
