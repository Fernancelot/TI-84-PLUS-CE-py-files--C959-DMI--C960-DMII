# EXPONENT_DECOMPOSER.py: Decompose Exponents into Smaller Powers
# Purpose:
# This program takes an input base (b) and an exponent (e) and decomposes the exponent
# into a sum of powers of 2. It then expresses the result as a product of powers of b.

# Function to decompose an exponent into powers of 2
def decompose_exponent(base, exponent):
    components = []
    power = 0

    while exponent > 0:
        if exponent % 2 == 1:
            components.append(power)
        exponent //= 2
        power += 1

    return components

# Function to format the result as a product of powers
def format_result(base, components):
    terms = []
    for exp in components[::-1]:
        terms.append(str(base) + "^" + str(2 ** exp))
    return " × ".join(terms)

def main():
    print("Exponent Decomposer")
    print("Decomposes a base and exponent into a product of smaller powers.")

    try:
        # Input base and exponent
        base = int(input("Enter the base (e.g., 4): "))
        exponent = int(input("Enter the exponent (e.g., 230): "))

        if base <= 0 or exponent <= 0:
            print("Error: Base and exponent must be positive integers.")
            return

        # Decompose the exponent
        components = decompose_exponent(base, exponent)

        # Format and display the result
        result = format_result(base, components)
        print(str(base) + "^" + str(exponent) + " = " + result)

    except ValueError:
        print("Error: Please enter valid integers for base and exponent.")

if __name__ == "__main__":
    main()
