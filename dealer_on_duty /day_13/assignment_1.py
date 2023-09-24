import string


def is_pangram(text: str) -> bool:
    if not string:
        return False

    alphabet = set(string.ascii_lowercase)
    text = text.lower()

    for char in text:
        if char in alphabet:
            alphabet.remove(char)

    return not alphabet


if __name__ == '__main__':
    input_text = input('Enter a words or sentences to check if it pangram. ')

    state = 'not '
    if is_pangram(input_text):
        state = ''
    print(f'The text is {state}pangram')
