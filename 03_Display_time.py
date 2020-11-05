# Write a simple program to display time using operator // and %

# Prompt user for input
seconds = int(input("Enter an integer for seconds : "))

# Get minutes and remaining seconds
minutes = seconds // 60             # Find minutes in seconds
remaining_seconds = seconds % 60    # seconds remaining

# Display time
print(f"{seconds} is {minutes} minutes and {remaining_seconds} seconds")