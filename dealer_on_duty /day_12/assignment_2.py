def longest_word_and_length(words: list) -> tuple:
    if not words:
        return None, 0

    longest_word = ""
    max_length = 0

    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    return longest_word, max_length


if __name__ == '__main__':
    input_list = input('Enter words. ').split()
    longest_word, length = longest_word_and_length(input_list)
    print('Longest word:', longest_word)
    print('Length of longest word:', length)

