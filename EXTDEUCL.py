# UNIT 2: MODULE 5: Extended Euclidean Algorithm
# Purpose:
# This program calculates the GCD (Greatest Common Divisor) of two integers
# using the Extended Euclidean Algorithm. It also finds coefficients x and y
# such that ax + by = gcd(a, b).

# Usage and Instructions:
# - Input two integers (a and b).
# - The program calculates and displays:
#   - The GCD of a and b.
#   - Coefficients x and y for the linear combination.
#   - Whether a multiplicative inverse exists and its value, if applicable.
#   - Additionally, the program displays the values of integers a and b correctly matched to the inputs.


def extended_euclid(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_euclid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

def multiplicative_inverse_exists(a, b):
    gcd, _, _ = extended_euclid(a, b)
    return gcd == 1

def main():
    print("Extended Euclidean Algorithm")
    
    try:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
    except ValueError:
        print("Please enter valid integers.")
        return
    
    gcd, x, y = extended_euclid(a, b)
    print("GCD:", gcd)
    print("Coefficients x and y are:", y, "and", x)
    print("Integer a (coefficient for", a, ") is:", y)
    print("Integer b (coefficient for", b, ") is:", x)

    if multiplicative_inverse_exists(a, b):
        inverse = x % b
        print("Multiplicative Inverse EXISTS")
        print("The inverse of " + str(a) + " mod " + str(b) + " is " + str(inverse))
    else:
        print("Multiplicative Inverse DOES NOT EXIST")

main()







