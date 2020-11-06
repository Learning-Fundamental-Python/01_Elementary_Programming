# Write a program like financial application
# for count investment amount

# Prompt the user to enter final account value
final_account_value = eval(input('Enter final account value : '))

# Prompt the user to enter annual interest rate per one year
annual_interest_rate = eval(input('Enter annual interest rate in percent : '))

# Prompt the user to enter number of years interest rate
number_ofYears = eval(input("Enter number of years : "))

number_ofMonth = number_ofYears * 12
monthly_interestRate = (annual_interest_rate / 12) / 100

# Compute initial deposit amount
initial_depositAmount = final_account_value / ((1 + monthly_interestRate) ** number_ofMonth)

# Display the result
print(f"Initial deposit value is ${initial_depositAmount:.3f}")
