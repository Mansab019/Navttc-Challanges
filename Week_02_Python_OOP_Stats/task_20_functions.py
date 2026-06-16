# Task 20 - User Defined Functions
# Reference: https://www.geeksforgeeks.org/functions-in-python/

# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Mansab"))

# Function with default argument
def power(base, exp=2):
    return base ** exp

print(power(3))       # 9
print(power(2, 10))   # 1024

# Lambda expression
square = lambda x: x * x
print(square(5))

# Map and Filter
numbers = [1, 2, 3, 4, 5, 6]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Squared:", squared)
print("Evens:", evens)

# Inner/Nested function
def outer():
    def inner():
        print("I am inner function")
    inner()

outer()
