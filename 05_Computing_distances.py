# Write a simple program to compute and display the distance between two points

# Enter the first point with two floats values
x1, y1 = eval(input('Enter x1 and y1 for Point 1 : '))

# Enter the second point with two float values
x2, y2 = eval(input('Enter x2 and y2 for Point 2 : '))

# Compute the distance
distance = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5

# Display the results
print(f"The distance between two points is {distance:.2f}")