# Global conversion factors - note the exact spacing
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)  # Parentheses with exact spacing

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Main program function"""
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ").strip()
        if not temp_input.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        temperature = float(temp_input)

        # Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit not in ('C', 'F'):
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

        # Perform conversion
        if unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
