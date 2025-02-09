# UNIT 2: Fast Modular Exponentiation
# Purpose:
# This program computes modular exponentiation efficiently using successive squaring.

def modular_exponentiation(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def main():
    print("Fast Modular Exponentiation Program")
    base = int(input("Enter the base: "))
    exp = int(input("Enter the exponent: "))
    mod = int(input("Enter the modulo: "))
    result = modular_exponentiation(base, exp, mod)
    print("Result: " + str(result))

main()
