# Temperature Conversion Functions

def convertFahrenheit():
    try:
        fahrenheit = float(input("Enter the Fahrenheit temperature " +
                                 "to convert to Celsius: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"\nThe temperature in Celsius is {celsius:.2f}C.\n")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.\n")

def convertCelsius():
    try:
        celsius = float(input(f"Enter the Celsius temperature " +
                              "to convert to Fahrenheit: "))
        celsius = float(celsius)
        fahrenheit = (celsius/(5/9)) + 32
        print(f"\nThe temperature in Fahrenheit is {fahrenheit:.2f}F.\n")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.\n")

def displayMenu():
    print("""Choose operation:
        (1) Convert Fahrenheit to Celsius
        (2) Convert Celsius to Farenheit
        (3) Quit Program
        """)
