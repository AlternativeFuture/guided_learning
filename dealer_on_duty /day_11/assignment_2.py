def roman_to_decimal(roman_numeral):
    roman_to_decimal_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    decimal_number = 0
    prev_value = 0

    for char in roman_numeral[::-1]:  # Reverse traversal of the Roman numeral
        current_value = roman_to_decimal_dict[char]

        if current_value >= prev_value:
            decimal_number += current_value
        else:
            decimal_number -= current_value

        prev_value = current_value

    return decimal_number


if __name__ == "__main__":
    roman_numeral = input("Enter a Roman numeral (up to 3999): ").upper()

    try:
        decimal_number = roman_to_decimal(roman_numeral)
        print("Decimal equivalent:", decimal_number)
    except KeyError:
        print("Invalid Roman numeral. Please enter a valid Roman numeral.")
