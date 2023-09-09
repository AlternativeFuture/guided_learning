def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5/9


if __name__ == "__main__":
    print("Temperature Conversion Program")
    temperature = float(input("Enter the temperature value: "))
    input_scale = input("Enter the input temperature scale (C or F): ").upper()
    output_scale = input("Enter the output temperature scale (C or F): ").upper()

    if input_scale == "C" and output_scale == "F":
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result}°F")
    elif input_scale == "F" and output_scale == "C":
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result}°C")
    elif input_scale == "C" and output_scale == "C":
        print("Input and output scales are the same. No conversion needed.")
    elif input_scale == "F" and output_scale == "F":
        print("Input and output scales are the same. No conversion needed.")
    else:
        print("Invalid input or output temperature scale. Please use 'C' for Celsius or 'F' for Fahrenheit.")
