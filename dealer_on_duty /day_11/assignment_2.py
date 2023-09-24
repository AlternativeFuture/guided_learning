def is_password_long(text: str) -> bool:
    return len(text) > 8


def is_mix_letters(text: str) -> bool:
    return text != text.upper() and text != text.lower()


def contains_number(text: str) -> bool:
    return any(char.isdigit() for char in text)


def contains_special_character(text: str) -> bool:
    special_characters = '!@#$%^&*()_+*/?,.<>/;:'
    return any(char for char in text if char in special_characters)


if __name__ == '__main__':
    input_message = ('.The password should be at least 8 characters long. \n .It should contain a mix of uppercase '
                     'and lowercase letters. \n .It should include at least one digit (0-9). \n .It should include at '
                     'least one special character (e.g., !, @, #, $, %, etc.). \n Enter a valid password. ')

    security_options = {0: 'Weak', 1: 'Weak', 2: 'Moderate', 3: 'Strong', 4: 'Very Strong'}

    password = input(input_message)
    security_level = (is_password_long(password) + is_mix_letters(password) + contains_number(password) +
                      contains_special_character(password))

    print(f'The password is {security_options[security_level]}')
