def find_missing_number(array: tuple) -> int:
    total = sum(array)
    full_array_total = sum(x for x in range(1, max(array) + 1))
    return full_array_total - total


if __name__ == '__main__':
    input_array = input('Enter numbers. ').split()
    try:
        input_array = tuple(map(int, input_array))
    except ValueError as e:
        print(f'Invalid input. Please enter valid integers. {e}')
    else:
        print(find_missing_number(input_array))

