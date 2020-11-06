# Write a simple program to compute the the digits in an integer
# between 0 and 100 and adds all the digits in the integer

number = int(input('Enter a number between 0 and 1000 : '))

# Extract the digit and then compute all the digits
number_1 = number % 10
number_2 = number // 10
number_3 = number_2 // 10
number_4 = number_2 % 10

total_digits = number_1 + number_3 + number_4

# Display the result
print(f"The sum, of the digits is {total_digits}")
