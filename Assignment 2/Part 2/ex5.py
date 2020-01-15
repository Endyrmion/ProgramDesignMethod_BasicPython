# 5. Write a function called convert temp() that takes no arguments.
# This function obtains a temperature in Fahrenheit from the user and uses two helper functions to convert this temperature to Celsius and Kelvin.
# Write a helper function called convert to celsius() that takes a single argument in Fahrenheit and returns the temperature in Celsius using the formula
#
#  Tc = 5/9 ( Tf - 32)
#
# Where Tc  is the temperature in Celsius and Tf  is the temperature in Fahrenheit.
#
# Tk = Tc + 273.15
#
# Write another helper function called convert to kelvin() that takes a single argument in degrees Celsius and returns degrees Kelvin using the formula
# Where Tk is the temperature in Kelvin.
# Use these two functions within your convert temp() function to display (i.e., print) the temperatures for the user.
# The convert temp() does not return anything.
# The following demonstrates the proper behavior of this function:
# convert_temp()
# Enter a temperature in Fahrenheit: 32
# The temperature in Fahrenheit is: 32
# The temperature in Celsius is: 0.0
# The temperature in Kelvin is: 273.15
# convert_temp()
# Enter a temperature in Fahrenheit: 80
#
# The temperature in Fahrenheit is: 80
# The temperature in Celsius is: 26.666666666666668
# The temperature in Kelvin is: 299.81666666666666


def farhenToCel(farTemp):
    return (5 / 9 * (farTemp - 32))


def celsiusToKelv(celsiusTemp):
    return celsiusTemp + 273.15


def temp():
    try:
        farhenTemp = float(input("Fahrenheit?\n-> "))
    except:
        print("Wrong Input !")
        exit()
    celsiusTemp = farhenToCel(farhenTemp)
    print("The temperature in Fahrenheit is %f" % farhenTemp)  # The temperature in Fahrenheit is: 80
    print("The temperature in Celsius is %f" % celsiusTemp)  # The temperature in Celsius is: 26.666666666666668
    print("The temperature in Kelvin is %f" % celsiusToKelv(
        celsiusTemp))  # The temperature in Kelvin is: 299.81666666666666


temp()
