# Write a simple program to compute area of a triangle
import math

x1, y1 = eval(input("Enter the first point of side triangle : "))
x2, y2 = eval(input("Enter the second point of side triangle : "))
x3, y3 = eval(input("Enter the third point of side triangle : "))

side_1 = (y1 - x1)
side_2 = (y2 - x2)
side_3 = (y3 - x3)

# The formula
s = (side_1 + side_2 + side_3) / 2
area = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))

print(f"The area of the triangle is {area}")
