from collections import Counter
from statistics import mean, median


def calculate_mean_median_mode(numbers: list) -> tuple:
    mean_value = mean(numbers)
    median_value = median(numbers)
    counter = Counter(numbers)
    mode_values = [k for k, v in counter.items() if v == max(counter.values())]

    return mean_value, median_value, mode_values


if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")
    nums = [int(num) for num in user_input.split()]

    mean_value, median_value, mode_values = calculate_mean_median_mode(nums)

    print("Mean:", mean_value)
    print("Median:", median_value)
    print("Mode:", mode_values)
