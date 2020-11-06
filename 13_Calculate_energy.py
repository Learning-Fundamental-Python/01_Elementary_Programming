"""
Write a program that calculates the energy needed to
heat water from an initial temperature to a final temperature
"""

# Prompt user to input water in kilograms, initial temp and final temp
M = float(input('Enter the amount of water in kilograms : '))
initial_temp = float(input('Enter the initial temperature : '))
final_temp = float(input('Enter the final temperature : '))

'''
the formula to compute the energy is
Q = M * (finalTemperature – initialTemperature) * 4184
'''


# Q = Measured in joules
# temperature in Celcius
# M = the weight of water in kilograms

# Compute the energy
Q = M * (final_temp - initial_temp) * 4184

# Display the results
print(f"The energy needed is {Q:.1f} joules")
