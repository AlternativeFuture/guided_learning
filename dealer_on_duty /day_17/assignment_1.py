def color_invert(rgb_array: list) -> list:
    return [255 - x for x in rgb_array]


if __name__ == '__main__':
    print("Enter the RGB values as space-separated numbers.")
    input_array = input('Enter 3 numbers (R G B): ').split()
    try:
        input_array = list(map(int, input_array))
    except ValueError as e:
        print(f'Invalid input. Please enter valid integers. {e}')
    else:
        if len(input_array) != 3:
            print('Invalid input. Please enter exactly 3 numbers for R, G, and B.')
        else:
            inverted_array = color_invert(input_array)
            print('Inverted RGB values:', inverted_array)
