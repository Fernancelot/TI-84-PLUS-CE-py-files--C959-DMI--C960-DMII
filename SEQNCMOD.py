# Sequence Modulo Solver
# Purpose:
# This program calculates the value of a_n based on the recursive sequence defined by modulo 3 rules.
# Specifically:
# - a_{n+1} = a_n / 3 if a_n % 3 == 0
# - a_{n+1} = (a_n - 1) / 3 if a_n % 3 == 1
# - a_{n+1} = (a_n + 1) / 3 if a_n % 3 == 2

# Function to compute the sequence up to a specific term
def calculate_sequence(a1, target_term):
    current_value = a1

    for n in range(1, target_term):  # Calculate up to a_target_term
        if current_value % 3 == 0:
            current_value = current_value // 3
        elif current_value % 3 == 1:
            current_value = (current_value - 1) // 3
        elif current_value % 3 == 2:
            current_value = (current_value + 1) // 3

    return current_value

def main():
    print("Sequence Modulo Solver")
    print("This program computes the value of a_n based on a recursive sequence defined by modulo 3 rules.")

    try:
        # Input the initial value a1
        a1 = int(input("Enter the initial value (a1): "))
        target_term = int(input("Enter the target term (n): "))

        if a1 < 0 or target_term < 1:
            print("Error: Initial value must be non-negative and target term must be at least 1.")
            return

        # Compute the result
        result = calculate_sequence(a1, target_term)

        # Display the result
        print("The value of a_" + str(target_term) + " is:", result)

    except ValueError:
        print("Error: Please enter valid integers.")

if __name__ == "__main__":
    main()
