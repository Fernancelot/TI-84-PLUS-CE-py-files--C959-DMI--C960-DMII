# Explicit Recurrence Relation Solver
# Purpose:
# This program calculates the explicit form of a recurrence relation given in the form:
# a_(n+1) = a_n + d, with a_0 = initial_value.
# It evaluates a_n for a given n and provides the explicit formula.

# Function to calculate a_n for the recurrence relation
def calculate_recurrence(n, initial_value, difference):
    return initial_value + n * difference

def explicit_formula(initial_value, difference):
    return "a_n = " + str(initial_value) + " + " + str(difference) + "n"

def main():
    print("Explicit Recurrence Relation Solver")
    print("This program calculates the explicit form of a recurrence relation and evaluates it.")

    try:
        # Input initial value, difference, and n
        initial_value = int(input("Enter the initial value (a_0): "))
        difference = int(input("Enter the difference (d): "))
        n = int(input("Enter the term number (n): "))

        if n < 0:
            print("Error: n must be a non-negative integer.")
            return

        # Compute the explicit form and the result
        result = calculate_recurrence(n, initial_value, difference)
        formula = explicit_formula(initial_value, difference)

        # Display the results
        print("Explicit Formula: " + formula)
        print("The value of a_" + str(n) + " is: " + str(result))

    except ValueError:
        print("Error: Please enter valid integers.")

if __name__ == "__main__":
    main()
