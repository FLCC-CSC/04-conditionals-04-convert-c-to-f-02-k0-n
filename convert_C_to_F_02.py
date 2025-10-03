# FILE NAME - convert_C_to_F_02.py

# NAME: Josh Fielding
# DATE: 10/2/25 
# BRIEF DESCRIPTION: Convert C to F or F to C based on user input



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Temperature Converter =====")

print("\n  1. Convert from Celsius to Fahrenheit \n  2. Convert from Fahrenheit to Celsius")

choice = int(input("\nPlease choose from the above menu: "))

if choice == 1:
  celsius = float(input("Enter a temperature to convert: "))
  fahrenheit = celsius * 9/5 + 32
  print(f"\n{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.")
if choice == 2:
  fahrenheit = float(input("Enter a temperature to convert: "))
  celsius = (fahrenheit - 32) * 5/9
  print(f"\n{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius.")  


########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

I shouldn't second guess myself all the time because I had a feeling it was two 'if' statements, 
but didn't write it down at first for some reason.





'''
