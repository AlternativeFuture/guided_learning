if __name__ == '__main__':
    input_array = input('Enter numbers. ').split()
    try:
        input_array = tuple(map(int, input_array))
    except ValueError as e:
        print(f'Invalid input. Please enter valid integers. {e}')
    else:
        print(list(set(input_array)))
