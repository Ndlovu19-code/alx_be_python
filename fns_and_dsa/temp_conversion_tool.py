# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_INTERCEPT = 32
CELSIUS_TO_FAHRENHEIT_INTERCEPT = 0  # Correction: Intercept for Celsius to Fahrenheit should be 0

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global conversion factors."""
    celsius = (fahrenheit - FAHRENHEIT_TO_CELSIUS_INTERCEPT) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global conversion factors."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_TO_FAHRENHEIT_INTERCEPT
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature: "))
        unit = input("Is the temperature in Celsius or Fahrenheit (C/F)? ").strip().upper()

        if unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
        elif unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
        else:
            print("Invalid unit. Please enter "C" for Celsius or "F" for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()




       



