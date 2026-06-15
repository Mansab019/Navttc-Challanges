# Task 11 - Basic if statement

i = 10
if (i > 15):
    print("10 is less than 15")
print("I am Not in if")

# -----------------------------------------------

# Task 12 - if-else statement

i = 20
if (i < 15):
    print("i is smaller than 15")
    print("i'm in if Block")
else:
    print("i is greater than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")

# -----------------------------------------------

# Task 13 - Nested if statement

i = 10
if (i == 10):
    if (i < 15):
        print("i is smaller than 15")
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

# -----------------------------------------------

# Task 14 - if-elif-else ladder

i = 20
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")
