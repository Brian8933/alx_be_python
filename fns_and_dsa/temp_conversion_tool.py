#!/usr/bin/env python3
"""
Temperature Conversion Tool
Demonstrates variable scope by converting between Celsius and Fahrenheit
using global conversion factors.
"""

# Global conversion factors as required
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using global factor
    Args:
        fahrenheit: Temperature in Fahrenheit
    Returns:
        Temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using global factor
    Args:
        celsius: Temperature in Celsius
    Returns:
        Temperature in Fahrenheit
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def get_temperature_input():
    """
    Get and validate temperature input from user
    Returns:
        Validated temperature as float
    Raises:
        ValueError if input is not numeric
    """
    temp_input = input("Enter the temperature to convert: ").strip()
    if not temp_input.replace('.', '', 1).isdigit():
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return float(temp_input)

def get_unit_input():
    """
    Get and validate unit input from user
    Returns:
        Validated unit ('C' or 'F')
    Raises:
        ValueError if input is not C or F
    """
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit not in ('C', 'F'):
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    return unit

def main():
    """Main program execution"""
    try:
        temperature = get_temperature_input()
        unit = get_unit_input()

        if unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()