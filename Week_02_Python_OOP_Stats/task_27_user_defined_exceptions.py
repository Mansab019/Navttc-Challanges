# Task 27 - User Defined Exception Handling
# Reference: https://www.programiz.com/python-programming/user-defined-exception

# Custom exception class
class NegativeAgeError(Exception):
    def __init__(self, age, message="Age cannot be negative"):
        self.age = age
        self.message = message
        super().__init__(self.message)

class InvalidSalaryError(Exception):
    def __init__(self, salary, message="Salary must be greater than zero"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

# Using custom exceptions
def set_age(age):
    if age < 0:
        raise NegativeAgeError(age)
    print(f"Age set to: {age}")

def set_salary(salary):
    if salary <= 0:
        raise InvalidSalaryError(salary)
    print(f"Salary set to: {salary}")

try:
    set_age(-3)
except NegativeAgeError as e:
    print(f"Custom Error: {e}")

try:
    set_salary(-5000)
except InvalidSalaryError as e:
    print(f"Custom Error: {e}")
