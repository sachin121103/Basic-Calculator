import math

# Define the functions
def add(a,b):
    return a+b


def subtract(a,b):
    return a-b


def multiply (a,b):
    return a*b


def divide (a,b):
    return a/b


def factorial(a):
    multiply_count = 1
    for i in range(1, a+1):
        multiply_count = multiply_count*i
    return multiply_count


def square(a):
    return a**2


def square_root(a):
    if a >= 0:
        return a**0.5
    else:
        print("Please enter a positive number")

      
# print statements

print("Select your operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Factorial")
print("6. Square Root")
print("7. Square of a Number")

# Calculations
while True:
    
    try: 
        acceptable_input = [1, 2, 3, 4, 5, 6, 7]

        choice = int(input("Enter a number between 1-7: "))

        if choice in acceptable_input:

            if choice == 1:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    total = add(num1, num2)
                    print(total)
                except ValueError:
                    print("Please enter numbers")

            if choice == 2:
                try: 
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    subtraction = subtract(num1, num2)
                    print(subtraction)
                except ValueError:
                    print("Please enter numbers")

            if choice == 3:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    multiplication = multiply(num1, num2)
                    print(multiplication)
                except ValueError:
                    print("Please enter numbers")

            if choice == 4:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    division = divide(num1, num2)
                    print(division)
                except ValueError:
                    print("Please enter numbers")
                except ZeroDivisionError:
                    print("We cannot divide by 0! That breaks the universe. Change the value of the second number")
            if choice == 5:
                try:
                    num1 = int(input("Enter an integer: "))
                    factorialisation = factorial(num1)
                    print(factorialisation)
                except ValueError:
                    print("Please enter a whole number")
            if choice == 6:
                try:
                    num1 = float(input("Enter a number: "))
                    square_root_of_number = square_root(num1)
                    print(square_root_of_number)
                except ValueError:
                    print("Please enter numbers")
            if choice == 7:
                try:
                    num1 = float(input("Enter a number: "))
                    square_of_number = square(num1)
                    print(square_of_number)
                except ValueError:
                    print("Please enter numbers")
        else:
            print("You have entered unacceptable input. Enter a number in the range")
    except ValueError:
        print("Please enter a whole number")
