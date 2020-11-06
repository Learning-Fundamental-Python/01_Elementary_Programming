# Write a simple program to compute the wind - chill temperature index

# Prompt user to enter value degree of Fahrenheit
# between -58 and 41
fahrenheit = float(input("Enter the temperature in Fahrenheit "
                         "between -58 and 41 : "))

# Prompt user to enter the wind speed in miles per hour
wind_speed = float(input("Enter the wind speed in"
                         "miles per hour : "))

# Compute the wind chill index
wind_chill_tempIndex = 35.74 + (0.6215 * fahrenheit) \
                       - 35.75 * (wind_speed ** 0.16) \
                       + 0.4275 * fahrenheit * (wind_speed ** 0.16)

# Display the result
print(f"The wind chill index is {wind_chill_tempIndex:.3f}")
