# UNIT 2: MODULE 4: Standard Euclidean Algorithm for GCD
# Purpose:
# This program calculates the GCD (Greatest Common Divisor) of two integers
# using the Euclidean Algorithm. It also displays each step of the calculation.

# Usage and Instructions:
# - Input two integers (a and b).
# - The program calculates and displays:
#   - The GCD of a and b.
#   - The division steps as formulas.

def euclidean_algorithm(a, b):
    steps = []
    while b != 0:
        quotient = a // b
        remainder = a % b
        steps.append(str(a) + " = " + str(b) + " * " + str(quotient) + " + " + str(remainder))
        a, b = b, remainder
    return a, steps

def main():
    print("Calculating GCD using the Euclidean Algorithm")
    try:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    gcd, steps = euclidean_algorithm(a, b)
    print("GCD: " + str(gcd))
    for step in steps:
        print(step)

main()
