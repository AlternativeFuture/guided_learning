def replace_first_char_occurrences(string: str) -> str:
    if not string:
        return ''

    first_char = string[0]
    modified_string = first_char + string[1:].replace(first_char, '$')

    return modified_string


if __name__ == '__main__':
    input_word = input('Enter a word. ')

    result = replace_first_char_occurrences(input_word)
    print('Modified String:', result)
