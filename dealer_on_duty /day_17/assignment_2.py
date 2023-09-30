def number_length_and_sum_of_digits(number: int) -> tuple:
    number = abs(number)
    if number == 0:
        return 1, 0

    length = 0
    sum_of_digits = 0

    while number > 0:
        length += 1
        number, remainder = divmod(number, 10)
        sum_of_digits += remainder
    return length, sum_of_digits


if __name__ == '__main__':
    try:
        input_number = int(input('Enter a number. '))
    except ValueError as e:
        print(f'Invalid input. Please enter valid integers. {e}')
    else:
        print(number_length_and_sum_of_digits(input_number))

