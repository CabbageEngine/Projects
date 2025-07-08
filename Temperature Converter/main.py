from temp_converter import *

# Main program for temperature converter

'''
Create a module that contains two functions:
    fahrenheit to celsius(temp f)
    celsius to fahrenheit(temp c)

Main program should ask if user wants to covert from F to C and vice versa
Ask for the temperature and calls the right funciton. Prints the result.
'''

prompt = "Temperature Converter\n"
prompt += "Convert Fahrenheit to Celsius or Celsius to Fahrenheit\n"
print(prompt)


while True:
    displayMenu()
    choice = input("Choose an operation: ")

    if choice == '1':
        convertFahrenheit()
    elif choice == '2':
        convertCelsius()
    elif choice == '3':
        print("Thank You for using the Temperature Converter.")
        break
    else:
        print("That entry is not valid.")

