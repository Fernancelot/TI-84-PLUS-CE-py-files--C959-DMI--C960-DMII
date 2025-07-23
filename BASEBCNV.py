# UNIT 2: MODULE 6: Number Representation In Other Bases
# Purpose:
# This program converts a positive integer from one base to another.
# It supports alphanumeric digits for bases greater than 10 (e.g., base 16).
# It validates the inputs to ensure that the digits are valid for the specified base.
# The steps are as follows:
# 1. Convert the number from the input base (b) to base 10.
# 2. Convert the resulting base 10 number to the desired output base (b2).
# 3. Display the results in a clear format.

# Function to convert a single digit to its decimal value
# This supports both numeric and alphanumeric digits (e.g., 'A' = 10 in base 16).
# If the digit is invalid for the base, it returns -1.
def digit_to_val(digit):
    if '0' <= digit <= '9':  # Numeric digit
        return ord(digit) - ord('0')  # Convert ASCII to decimal
    elif 'A' <= digit.upper() <= 'F':  # Alphanumeric digit
        return ord(digit.upper()) - ord('A') + 10  # Convert A-F to decimal (10-15)
    else:
        return -1  # Invalid digit

# Function to convert a number from base b to base 10
# Parameters:
# n0The number as a string (e.g., "1A3" for base 16).
# b: The base of the number n (e.g., 16 for hexadecimal).
# Returns:
# The equivalent decimal value of n, or -1 if n contains invalid digits for base b.
def base_b_to_10(n, b):
    n10 = 0  # Initialize the result as 0
    for digit in n:
        val = digit_to_val(digit)  # Get the decimal value of the digit
        if val < 0 or val >= b:  # Check if the digit is invalid for the base
            return -1  # Return -1 for invalid input
        n10 = n10 * b + val  # Update the result using positional notation
    return n10

# Function to convert a number from base 10 to another base (b2)
# Parameters:
# n10: The number in base 10.
# b2: The base to convert to (e.g., 16 for hexadecimal).
# Returns:
# The number as a string in the new base, including alphanumeric digits for bases > 10.
def base_10_to_b2(n10, b2):
    digits = []  # List to store the digits of the new base
    while n10 > 0:
        remainder = n10 % b2  # Get the remainder
        if remainder >= 10:  # Convert remainder to alphanumeric character if needed
            digits.append(chr(remainder - 10 + ord('A')))
        else:  # Add numeric remainder
            digits.append(str(remainder))
        n10 //= b2  # Reduce n10 for the next iteration
    if not digits:  # Handle the case where n10 is 0
        digits.append('0')
    digits.reverse()  # Reverse the digits to get the correct order
    return ''.join(digits)  # Join the digits into a single string

# Main function to take user inputs and perform the conversion
def main():
    # Introduction and explanation
    print("Base Conversion Program")
    print("This program converts a number from one base to another.")
    print("For bases greater than 10, use uppercase letters (A-F) for digits.")
    
    try:
        # Input for the number, its base, and the target base
        n = input("Enter the number to convert (e.g., 1A3 for base 16): ")
        b = int(input("Enter the base of the input number (b > 1): "))
        b2 = int(input("Enter the base to convert to (b2 > 1): "))
    except ValueError:
        # Handle invalid inputs for the bases
        print("Invalid input. Please enter valid integers for the bases.")
        return

    # Convert the number from base b to base 10
    n10 = base_b_to_10(n, b)
    if n10 < 0:  # Check for invalid digits in the input number
        print("Invalid number for the given base.")
    else:
        # Convert the base 10 number to the target base (b2)
        result = base_10_to_b2(n10, b2)
        # Display the result (replacing the f-string with concatenation)
        print("The number " + n + " in base " + str(b) + " is " + result + " in base " + str(b2) + ".")

# Call the main function to run the program
main()







