# Write a simple program to compute average of three numbers

print('Example 01 : ')
# Prompt user to enter three numbers
number1 = int(input('Enter the first number : '))
number2 = int(input('Enter the second number : '))
number3 = int(input('Enter the third number : '))

# Compute Average
average = (number1 + number2 + number3) / 3

# Display the result
print(f"The Average of {number1}, {number2}, {number3} is {average}")
print()

print('Example 02 : ')
# Prompt user to enter three numbers
# using simultaneous assignment
number1, number2, number3 = eval(input("Enter three numbers separated by commas : "))

# Compute Average
average = (number1 + number2 + number3) / 3.0

# Display the result
print(f"The Average of {number1}, {number2}, {number3} is {average}")
