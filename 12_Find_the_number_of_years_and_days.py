"""
that prompts the user to enter the minutes (e.g., 1 billion),
and displays the number of years and days for the minutes.
"""

# Prompt the user to enter the minutes
minutes = int(input('Enter the number of minutes : '))

'''
1 hour = 60 minute
1 day = 60 * 24 hours = 1440 minutes
1 year = 1440 minutes * 365 days = 525600 minutes in one year
'''

# Compute process
minute_inYears = minutes // 525600
remainder_minutes = minutes % 525600
minute_inDays = remainder_minutes // 1440

# Display the results
print(f"{minutes} minutes is approximately {minute_inYears} years and {minute_inDays} days")
