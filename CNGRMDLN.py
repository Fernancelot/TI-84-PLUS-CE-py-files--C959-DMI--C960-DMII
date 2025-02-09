# UNIT 2: MODULE 4: Congruence Modulo Calculator 
# This program simplifies and calculates expressions using modular arithmetic.
# It computes the result of (a^exp + b) mod n and displays all calculation steps.

# Usage and Instructions:
# - Input values for:
#   - 'a': The base.
#   - 'exp': The exponent (defaults to 1 if left blank).
#   - 'b': The number to add (defaults to 0 if left blank).
#   - 'n': The modulo base.
# - The program calculates and displays the step-by-step simplifications.

# Optimized modular exponentiation function to handle large exponents
def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod  # Reduce base modulo n
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

def simplify_and_mod(a, a_exp, b, n):
    # Display the input equation
    print("(" + str(a) + "^" + str(a_exp) + " + " + str(b) + ") mod " + str(n))
    a = a % n  # Simplify a modulo n
    b = b % n  # Simplify b modulo n
    # Display the simplified values
    print("Simplified: (" + str(a) + "^" + str(a_exp) + " + " + str(b) + ") mod " + str(n))
    
    # Perform modular exponentiation
    exp_result = modular_exponentiation(a, a_exp, n)
    result = (exp_result + b) % n
    # Display the final result
    print("Final result: " + str(result))
    return result

def main():
    try:
        # User input
        a = int(input("Enter the first number: "))
        a_exp = input("Enter the exponent for the first number (press enter to skip): ")
        if a_exp == "":
            a_exp = 1
        else:
            a_exp = int(a_exp)
        b_input = input("Enter the second number (press enter to default to 0): ")
        if b_input == "":
            b = 0
        else:
            b = int(b_input)
        n = int(input("Enter the modulo: "))
    except ValueError:
        print("Invalid input. Please enter integers.")
        return

    # Compute and display the result
    result = simplify_and_mod(a, a_exp, b, n)
    input("The result is: " + str(result) + "\nPress Enter to exit.")

main()
