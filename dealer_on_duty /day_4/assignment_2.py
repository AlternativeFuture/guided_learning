from collections import defaultdict


def load_words(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()


def group_anagrams(words):
    anagram_groups = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)

    return sorted(anagram_groups.values(), key=len, reverse=True)


if __name__ == "__main__":
    filename = input('Please enter the file path for processing ')

    words = load_words(filename)

    anagram_groups = group_anagrams(words)

    for group in anagram_groups:
        if len(group) > 1:
            print(group)
