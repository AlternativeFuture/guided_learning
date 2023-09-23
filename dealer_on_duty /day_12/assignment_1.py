def factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1

    total = 1
    for n in range(1, num + 1):
        total *= n

    return total


if __name__ == '__main__':
    input_number = input("Enter a non-negative number! ")

    try:
        input_number = int(input_number)
    except KeyError:
        print('Invalid input! Please enter a number!')

    if input_number >= 0:
        print(f'Factorial of {input_number} = ', factorial(input_number))
    else:
        print('Invalid input! Enter a non-negative number!')
