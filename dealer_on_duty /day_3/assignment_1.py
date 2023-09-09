import random


def random_number() -> int:
    """
    Generate a random integer between 1 and 100 (inclusive).

    Returns:
        int: A random integer.
    """
    return random.randint(1, 100)


def valid_input() -> int:
    """
    Prompt the user for a valid integer input.

    Returns:
        int: The user's valid integer input.
    """
    user_guess = None
    try:
        user_guess = int(input("Guess the number (between 1 and 100): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    return user_guess


def number_guessing(secret_number: int, v_input: callable):
    """
    Play a number guessing game.

    Args:
        secret_number (int): The secret number to be guessed.
        v_input (callable): A function to validate and retrieve user input.

    Returns:
        None
    """
    attempts = 0

    while True:
        user_guess = v_input()
        if not isinstance(user_guess, int):
            continue

        attempts += 1
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    secret_number = random_number()
    number_guessing(secret_number=secret_number, v_input=valid_input)


