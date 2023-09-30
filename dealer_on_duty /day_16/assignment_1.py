import random


def generate_random_numbers() -> list:
    random_numbers = [random.randint(1, 100) for _ in range(20)]
    return random_numbers


if __name__ == '__main__':
    random_numbers_list = generate_random_numbers()

    print('Random numbers list:', random_numbers_list)
    print('Average:', sum(random_numbers_list) / len(random_numbers_list))
    sorted_numbers = sorted(random_numbers_list)
    print("Largest value:", sorted_numbers[-1])
    print("Smallest value:", sorted_numbers[0])
    print("Second largest value:", sorted_numbers[-2])
    print("Second smallest value:", sorted_numbers[1])
    print("Number of even numbers:", sum(1 for num in sorted_numbers if num % 2 == 0))
