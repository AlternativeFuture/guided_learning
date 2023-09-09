error_message = 'Invalid input! You should enter numbers or one of operators (+ - * /)! Try again!'


def calculator(num1: int, num2: int, operator: str) -> (int, float):
    """
    Perform basic arithmetic operations on two numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        operator (str): The operator (+, -, *, /) to perform the operation.

    Returns:
        int or float or str: The result of the operation or an error message for division by zero.
    """
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Division by zero is not allowed"
            return num1 / num2


if __name__ == '__main__':
    print('This is a simple calculator.')
    while True:
        num1 = input('Enter first number: ')
        if not num1.isdigit():
            print(error_message)
            continue
        num1 = int(num1)

        operator = input('Enter operator: ')
        if operator not in '+-*/':
            print(error_message)
            continue

        num2 = input('Enter second number: ')
        if not num2.isdigit():
            print(error_message)
            continue
        num2 = int(num2)

        result = calculator(num1, num2, operator)
        if isinstance(result, str):
            print(result)
        else:
            print(f'{num1} {operator} {num2} = {result}')
