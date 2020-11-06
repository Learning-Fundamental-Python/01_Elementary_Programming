# Write a simple program to Find minimum runway length
# of an plane to take off

# Prompt user for enter value of speed and acceleration of an plane
acceleration = float(input('Enter value acceleration of an plane : '))
speed = float(input('Enter value speed of an plane : '))

# compute minimum length runway
length = (speed ** 2) / (2 * acceleration)

# Display the result
print(f"The minimum runway length for this airplane is {length:.3f} meters")
