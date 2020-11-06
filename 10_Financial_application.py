# Write a simple program to compute the gratuity rate and total

# Prompt user for input subtotal and gratuity rate
# input two numbers separated by commas
subtotal, gratuity_rate = eval(input('Enter the subtotal and a gratuity rate : '))

# compute value of gratuity and the total
gratuity = (subtotal * gratuity_rate) / 100
total = subtotal + gratuity

# Display the result
print(f"The gratuity is {gratuity:.2f} and the total is {total:.2f}")