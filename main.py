# Task 1

# The greeting program.
# Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:
# “Good day <name>! <day> is a perfect day to learn some python.”
# Note that <name> and <day> are predefined variables in source code.
# An additional bonus will be to use different string formatting methods for constructing result string.

name = 'Victor'
day = '24.05.2021'

print(f'" Good day {name}!  {day} is a perfect day to learn some python."')


# Task 2
# Manipulate strings.
# Save your first and last name as separate variables, then use string concatenation to add them together with
# a white space in between and print a greeting.
first_name = 'Victor'
last_name = 'Nikoriak'

print(f'Привіт мене звати {first_name} {last_name}.')


# Task 3
# Using python as a calculator.
# Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:
# Addition
# Subtraction
# Division
# Multiplication
#Exponent (Power)
# Modulus
# Floor division


a = 2
b = 2

addition = a+b
subtraction = a-b
division = a/b
multiplication = a*b
exponent = a**b
modulus = a % b
floor_division = a//b

print(f'Addition a + b = {addition}')
print(f'Subtraction a - b = {subtraction}')
print(f'Division a / b = {division}')
print(f'Multiplication a * b = {multiplication}')
print(f'Exponent (Power) a ** b = {exponent}')
print(f'Modulus a % b = {modulus}')
print(f'Floor division a // b = {floor_division}')
