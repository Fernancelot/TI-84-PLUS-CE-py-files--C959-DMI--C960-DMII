# UNIT 2: MODULE 6: Decimal, Binary, Hexadecimal Converter
# Purpose:
# This program converts numbers between decimal, binary, and hexadecimal formats.
# It validates inputs to ensure they match the specified format (e.g., binary numbers only contain 0 and 1).
# The program also handles errors gracefully and provides feedback for invalid inputs.

# Usage and Instructions:
# - You will be prompted to:
#   1. Select the input type: Decimal (1), Binary (2), or Hexadecimal (3).
#   2. Enter the number in the specified format.
#   3. Select the desired output type: Decimal (1), Binary (2), or Hexadecimal (3).
# - The program will convert the number and display the result.
# - Enter valid numbers for the selected input type to avoid errors.

def is_valid_binary(binary_str):
    for char in binary_str:
        if char not in '01':
            return False
    return True

def is_valid_hexadecimal(hex_str):
    for char in hex_str.upper():
        if char not in '0123456789ABCDEF':
            return False
    return True

def convert_number(input_type, input_value, output_type):
    if input_type == 1:  # Decimal
        try:
            decimal_value = int(input_value)
        except ValueError:
            print("Invalid decimal input. Please enter a valid decimal number.")
            return False
    elif input_type == 2:  # Binary
        if not is_valid_binary(input_value):
            print("Invalid binary input. Please enter a valid binary number (0 and 1 only).")
            return False
        decimal_value = int(input_value, 2)
    elif input_type == 3:  # Hexadecimal
        if not is_valid_hexadecimal(input_value):
            print("Invalid hexadecimal input. Please enter a valid hexadecimal number (0-9 and A-F).")
            return False
        decimal_value = int(input_value, 16)
    else:
        print("Invalid input type. Please enter 1 for Decimal, 2 for Binary, or 3 for Hexadecimal.")
        return False

    if output_type == 1:  # Decimal
        output_value = str(decimal_value)
    elif output_type == 2:  # Binary
        output_value = bin(decimal_value)[2:]  # Remove the '0b' prefix
    elif output_type == 3:  # Hexadecimal
        output_value = hex(decimal_value)[2:].upper()  # Remove the '0x' prefix and convert to uppercase
    else:
        print("Invalid output type. Please enter 1 for Decimal, 2 for Binary, or 3 for Hexadecimal.")
        return False

    print("OUTPUT:", output_value)
    return True

def main():
    print("Decimal, Binary, Hexadecimal Converter")
    print("Convert numbers between decimal, binary, and hexadecimal formats.")
    
    while True:
        try:
            input_type = int(input("INPUT: Dec=1, Bin=2, Hex=3: "))
            if input_type not in [1, 2, 3]:
                raise ValueError("Invalid input type. Please enter 1, 2, or 3.")
            
            input_value = input("INPUT VARIABLE: ")
            
            output_type = int(input("OUTPUT: Dec=1, Bin=2, Hex=3: "))
            if output_type not in [1, 2, 3]:
                raise ValueError("Invalid output type. Please enter 1, 2, or 3.")

