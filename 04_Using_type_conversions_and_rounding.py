# Write a simple program to compute tax and rounding the result
print('Example 01 :')
# prompt user for input number (integer or float type)

purchase_amount = eval(input('Enter purchase amount : '))

# Compute sales tax
tax = purchase_amount * 0.06

# Display tax amount with two digits after decimal point
print(f"Sales tax is {int(tax * 100) / 100.0}")
print()

print('Example 02 :')
# prompt user for input number (integer or float type)

purchase_amount = eval(input('Enter purchase amount : '))

# Compute sales tax
tax = purchase_amount * 0.06

# Display tax amount with two digits after decimal point
print(f"Sales tax is {(tax * 100 / 100):.2f}")
