def to_scottish_screaming(txt: str) -> str:
    vowels = 'AEIOUaeiou'
    result = ''
    for char in txt:
        if char in vowels:
            result += 'E'
        else:
            result += char
    return result.upper()


if __name__ == "__main__":
    print(to_scottish_screaming("hello world"))
    print(to_scottish_screaming("Mr. Fox was very naughty"))
    print(to_scottish_screaming("Butterflies are beautiful!"))
