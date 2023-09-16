def calculate_statistics(numbers: list) -> tuple:
    total = sum(numbers)
    count = len(numbers)
    average = total / count

    return total, count, average


def user_input() -> list:
    numbers = []

    while True:
        u_input = input('Enter a number (or "done" to finish): ')

        if u_input.lower() == 'done':
            break

        try:
            number = float(u_input)
            numbers.append(number)
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    return numbers


if __name__ == "__main__":
    numbers = user_input()
    if numbers:
        total, count, average = calculate_statistics(numbers)
        print(f'Total: {total}')
        print(f'Count: {count}')
        print(f'Average: {average}')
    else:
        print("You did not enter eny number!")
