############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

print "Enter a number (celsius) that you want to convert to fahrenheit"
celsius = int(raw_input())
fahrenheit = celsius * 9 / 2 + 32
print fahrenheit
