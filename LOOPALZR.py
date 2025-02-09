# Nested Loop Analyzer
# Purpose:
# This program evaluates how many times a variable is modified within nested loops.
# Users can input the ranges for the loops and the operation performed in each iteration.

# Function to analyze nested loops
def nested_loop_analysis(outer_range, inner_range_start_func, inner_range_end, operation_func):
    modifications = 0
    global C
    C = 0  # Initialize the variable C (optional variable for calculations)

    # Outer loop
    for i in range(*outer_range):
        # Inner loop
        for j in range(inner_range_start_func(i), inner_range_end):
            exec("C = " + operation_func.replace("C", str(C)))  # Perform the operation
            modifications += 1  # Count the modification

    return modifications

def main():
    print("Nested Loop Analyzer")
    print("This program calculates how many times a variable is modified in nested loops.")

    try:
        # Input ranges for the outer loop
        outer_start = int(input("Enter the start of the outer loop range: "))
        outer_end = int(input("Enter the end of the outer loop range (exclusive): "))
        outer_range = (outer_start, outer_end)

        # Input ranges for the inner loop (as a function of the outer loop variable)
        inner_start_expression = input("Enter the start of the inner loop range as a function of i (e.g., 'i + 1'): ")
        inner_range_start_func = lambda i: eval(inner_start_expression, {"i": i})
        inner_end = int(input("Enter the end of the inner loop range (exclusive): "))

        # Define the operation performed in each iteration
        print("Enter the operation performed in each iteration (use 'C' for count, e.g., 'C + i * j').")
        operation_expression = input("Operation: ")

        # Analyze the nested loops
        modifications = nested_loop_analysis(outer_range, inner_range_start_func, inner_end, operation_expression)

        # Display the result
        print("The variable is modified", modifications, "times.")
        print("Final value of C:", C)

    except Exception as e:
        print("Error:", e)
        print("Please check your input and try again.")

if __name__ == "__main__":
    main()
