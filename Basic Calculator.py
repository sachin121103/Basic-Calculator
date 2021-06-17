import math

# Defining the functions
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


# Introduction to Calculator
print("Hello! Welcome to my calculator!)
print("Select your operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Factorial")
print("6. Square Root")
print("7. Square of a Number")

# Code to run for input
while True:
    acceptable_input = [1, 2, 3, 4, 5, 6, 7]

    choice = int(input("Enter a number between 1-7: "))
    
    if choice in acceptable_input:
        
        if choice == 1:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            total = add(num1, num2)
            print(total)
            
        if choice == 2:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            subtraction = subtract(num1, num2)
            print(subtraction)
                
        if choice == 3:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            multiplication = multiply(num1, num2)
            print(multiplication)
            
        if choice == 4:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            division = divide(num1, num2)
            print(division)
            
        if choice == 5:
            num1 = int(input("Enter a number: "))
            factorial_number = factorial(num1)
            print(factorial_number)
        
        if choice == 6:
            num1 = float(input("Enter a number: "))
            square_root_of_number = square_root(num1)
            print(square_root_of_number)
            
        if choice == 7:
            num1 = float(input("Enter a number: "))
            square_of_number = square(num1)
            print(square_of_number)
            
    else:
        print("You have entered unacceptable input")

