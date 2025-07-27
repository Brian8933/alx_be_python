# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Main program function handling user interaction"""
    while True:  # Loop until valid input is provided
        try:
            # Get temperature input
            temp_input = input("Enter the temperature to convert: ").strip()
            temperature = float(temp_input)

            # Get unit input with validation
            while True:
                unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
                if unit in ('C', 'F'):
                    break
                print("Invalid unit. Please enter 'C' or 'F'.")

            # Perform conversion and display result
            if unit == "C":
                result = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {result:.2f}°F")
            else:
                result = convert_to_celsius(temperature)
                print(f"{temperature}°F is {result:.2f}°C")
            
            break  # Exit the loop after successful conversion

        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    main()