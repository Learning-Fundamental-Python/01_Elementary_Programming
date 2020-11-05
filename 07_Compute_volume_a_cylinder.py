# Write a simple program to compute the volume of a cylinder

# Make a constant
PHI = 3.14159

# Prompt user for input radius of cylinder
radius = float(input('Enter the radius of a cylinder : '))

# Prompt user for input length of a cylinder
length = float(input('Enter the length of a cylinder : '))# Write a simple program to convert degree of Celcius to Farenheit

# Compute area of a cylinder
area = PHI * radius * radius

# Compute volume of cylinder
volume = area * length

# Display the result
print(f"The area is {area:.2f} m2")
print(f"The volume is {volume:.2f} m3")