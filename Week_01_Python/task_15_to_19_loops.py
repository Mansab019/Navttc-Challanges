# Task 15 - For Loops
# Reference: https://www.geeksforgeeks.org/python-for-loops/

for i in range(1, 6):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(3):
    print(i)
else:
    print("Loop finished!")

# -----------------------------------------------

# Task 16 - While Loops
# Reference: https://www.geeksforgeeks.org/python-while-loops/

count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# -----------------------------------------------

# Task 17 - Break Statement
# Reference: https://www.geeksforgeeks.org/python-break-statement/

for i in range(1, 10):
    if i == 5:
        print("Breaking at 5")
        break
    print(i)

# -----------------------------------------------

# Task 18 - Continue Statement
# Reference: https://www.geeksforgeeks.org/python-continue-statement/

for i in range(1, 10):
    if i == 5:
        print("Skipping 5")
        continue
    print(i)

# -----------------------------------------------

# Task 19 - Various Looping Techniques
# Reference: https://www.geeksforgeeks.org/looping-techniques-python/

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

names = ["Ali", "Sara", "Ahmed"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(name, "->", score)

student = {"name": "Mansab", "age": 21, "city": "Lahore"}
for key, value in student.items():
    print(key, ":", value)
