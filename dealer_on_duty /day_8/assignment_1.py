def print_diamond(n: int):
    # Upper Triangle
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)

    # Lower Triangle
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)


if __name__ == '__main__':
    print_diamond(5)
    print_diamond(9)
    print_diamond(21)
