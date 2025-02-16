"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1) When will a ValueError occur?
# Answer: This error will occur whenever the user input is not a valid number like if the user input a string
# 2) When will a ZeroDivisionError occur?
# Answer: The error will occur when the user input the denominator is 0
# 3) Could you change the code to avoid the possibility of a ZeroDivisionError?
# Answer: Added a while loop so that the user input is not 0