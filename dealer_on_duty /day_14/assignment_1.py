def fizz_buzz() -> list:
    list_range = [x for x in range(1, 21)]

    for x in list_range:
        if x % 3 == 0 and x % 5 == 0:
            list_range[x-1] = 'FizzBuzz'
        elif x % 3 == 0:
            list_range[x-1] = 'Fizz'
        elif x % 5 == 0:
            list_range[x-1] = 'Buzz'

    return list_range


if __name__ == '__main__':
    print(fizz_buzz())
