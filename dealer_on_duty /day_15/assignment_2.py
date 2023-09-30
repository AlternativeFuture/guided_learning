def is_x_power_y_within_interval(x: int, y: int, l: int, r: int) -> bool:
    if l >= r:
        print("Invalid interval. Please ensure l is less than r.")
        return False

    if x < 0 or y < 0:
        print("x and y must be non-negative integers.")
        return False

    return l <= x**y <= r


if __name__ == '__main__':
    try:
        input_x = int(input('Enter a number x. '))
        input_y = int(input('Enter a number y. '))
        input_l = int(input('Enter a number l. '))
        input_r = int(input('Enter a number r. '))
    except ValueError as e:
        print(f'Invalid input. Please enter valid integers. {e}')
    else:
        print(is_x_power_y_within_interval(input_x, input_y, input_l, input_r))

