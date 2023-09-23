from collections import Counter


def extract_elements_with_frequency_greater_than_k(array: list, key: int) -> list:
    element_counts = Counter(array)
    result = [element for element, count in element_counts.items() if count > key]

    return result


if __name__ == "__main__":
    test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
    k = 3
    output = extract_elements_with_frequency_greater_than_k(test_list, key=k)
    print("Output:", output)

    test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
    k = 2
    output = extract_elements_with_frequency_greater_than_k(test_list, key=k)
    print("Output:", output)
