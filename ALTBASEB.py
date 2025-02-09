# UNIT 2: Binary ↔ Hexadecimal Conversions
# Purpose:
# This program handles binary ↔ hexadecimal conversions directly.

def binary_to_hex(binary):
    decimal = int(binary, 2)
    return hex(decimal)[2:].upper()

def hex_to_binary(hexadecimal):
    decimal = int(hexadecimal, 16)
    return bin(decimal)[2:]

def main():
    print("Binary ↔ Hexadecimal Conversion Program")
    print("1: Binary to Hexadecimal")
    print("2: Hexadecimal to Binary")
    
    choice = int(input("Enter your choice (1 or 2): "))
    if choice == 1:
        binary = input("Enter binary number: ")
        result = binary_to_hex(binary)
        print("Hexadecimal: " + result)
    elif choice == 2:
        hexadecimal = input("Enter hexadecimal number: ")
        result = hex_to_binary(hexadecimal)
        print("Binary: " + result)
    else:
        print("Invalid choice.")

main()
