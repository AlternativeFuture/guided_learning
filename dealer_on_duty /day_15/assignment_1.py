def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for x in range(2, int(number ** 0.5) + 1):
        if number % x == 0:
            return False

    return True


if __name__ == '__main__':
    try:
        input_num = int(input('Enter a number that is higher than 1. '))
    except ValueError:
        print(False)
    else:
        print(is_prime(input_num))
