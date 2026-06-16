# Task 25 - Dictionary Data Type
# Reference: https://www.programiz.com/python-programming/dictionary

student = {
    "name": "Mansab Ali",
    "age": 21,
    "city": "Lahore",
    "skills": ["Python", "ML", "Django"]
}

# Access
print(student["name"])
print(student.get("age"))

# Update
student["age"] = 22
student["university"] = "Superior University"
print(student)

# Delete
del student["city"]
print(student)

# Loop
for key, value in student.items():
    print(f"{key}: {value}")

# Keys and Values
print(student.keys())
print(student.values())

# Nested dictionary
employees = {
    "emp1": {"name": "Ali", "salary": 50000},
    "emp2": {"name": "Sara", "salary": 60000}
}
print(employees["emp1"]["name"])
