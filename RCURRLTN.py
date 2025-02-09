# Recurrence Relation Calculator for TI-84 CE Plus Python Edition
# Users input the recurrence relation, initial terms, and the target term.
#
# Features:
# - Accepts user-defined recurrence relations (e.g., "4*p[n-1] - 2*n - 3").
# - Handles initial terms provided as a list (e.g., "p0=2,p1=1").
# - Computes terms iteratively to avoid memory issues.
#
# How to Use:
# 1. Input the recurrence relation (e.g., "4*p[n-1] - 2*n - 3").
# 2. Provide the initial terms (e.g., "p0=2,p1=1").
# 3. Enter the target term number to calculate (e.g., "6" for p6).
#
# Example:
# Recurrence Relation: "p[n-1] + 2*n"
# Initial Terms: "p0=1"
# Target Term: 4
# Output: Calculates p4 step-by-step and displays the final result.

def compute_recurrence():
    print("Recurrence Relation Calculator")
    print("Calculate terms of a recurrence relation step-by-step.")

    # Input the recurrence relation
    relation = input("Enter the recurrence relation (e.g., '4*p[n-1] - 2*n - 3'): ")

    # Parse initial terms
    initial_terms = input("Enter initial terms (comma-separated, e.g., 'p0=2,p1=1'): ").split(',')
    local_vars = {}
    for term in initial_terms:
        parts = term.split('=')
        if len(parts) != 2:
            print("Error: Invalid initial term format. Use 'p0=2,p1=1'.")
            return
        name = parts[0].strip()
        try:
            value = int(parts[1].strip())
        except ValueError:
            print("Error: Initial term values must be integers.")
            return
        local_vars[name] = value

    # Get the variable name (e.g., 'p') from the initial terms
    var_name = initial_terms[0][0]

    # Target term
    try:
        target_n = int(input("Enter the term to find (e.g., '6' for p6): "))
    except ValueError:
        print("Error: Target term must be an integer.")
        return

    # Create a dictionary to store calculated terms
    current_terms = {}
    for key, value in local_vars.items():
        idx = int(key[len(var_name):])  # Extract the index (e.g., '0' from 'p0')
        current_terms[idx] = value

    # Compute terms iteratively
    for n in range(len(local_vars), target_n + 1):
        # Replace '[var_name][n-1]' and '[var_name][n-2]' with actual values
        expr = relation
        if var_name + "[n-1]" in expr:
            expr = expr.replace(var_name + "[n-1]", str(current_terms.get(n - 1, 0)))
        if var_name + "[n-2]" in expr:
            expr = expr.replace(var_name + "[n-2]", str(current_terms.get(n - 2, 0)))
        expr = expr.replace("n", str(n))

        # Safely evaluate the expression
        try:
            p_n = eval(expr, {"__builtins__": None}, {})
        except Exception as e:
            print("Error evaluating the relation. Please check your input.")
            return

        # Store the result
        current_terms[n] = p_n
        print("Step " + str(n) + ": " + var_name + str(n) + " = " + expr + " = " + str(p_n))

    # Output the final result
    result = current_terms.get(target_n, None)
    if result is not None:
        print("\nThe value of " + var_name + str(target_n) + " is: " + str(result))
    else:
        print("Unable to calculate the requested term.")

compute_recurrence()
