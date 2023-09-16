def is_valid(s: str) -> bool:
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
        else:
            return False

    return len(stack) == 0


if __name__ == '__main__':
    print(is_valid('([)]'))
    print(is_valid('()'))
    print(is_valid('{}'))
    print(is_valid('[{}]'))
