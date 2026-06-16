# Task 26 - Exception Handling
# Reference: https://www.programiz.com/python-programming/exception-handling

# Basic try-except
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    print("This always runs.")

# Multiple exceptions
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"Index Error: {e}")

# Raise exception manually
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

try:
    check_age(-5)
except ValueError as e:
    print(e)
