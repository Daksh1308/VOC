def convert_temperature(value, unit):
    if unit == 'F':
        # Fahrenheit to Celsius
        celsius = (value - 32) * 5 / 9
        return round(celsius, 2)
    elif unit == 'C':
        # Celsius to Fahrenheit
        fahrenheit = (value * 9 / 5) + 32
        return round(fahrenheit, 2)
    else:
        return "Invalid unit. Use 'F' for Fahrenheit or 'C' for Celsius."

# Example usage:
print(convert_temperature(100, 'F'))  # Output should be 37.78
print(convert_temperature(0, 'C'))    # Output should be 32.0
