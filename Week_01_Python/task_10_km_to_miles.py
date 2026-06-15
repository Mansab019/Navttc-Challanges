# Task 10 - Convert Kilometers to Miles

kilometers = float(input("Enter value in kilometers: "))

# Conversion factor
conv_fac = 0.621371

# Calculate miles
miles = kilometers * conv_fac
print('%0.3f kilometers = %0.3f miles' % (kilometers, miles))
