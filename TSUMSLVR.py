# Telescoping Sum Solver
# Purpose:
# This program calculates the value of P(n) defined by the telescoping sum:
# P(n) = sum(k=1 to n) [1/k - 1/(k+1)]

# Function to compute the telescoping sum P(n)
def calculate_p(n):
    if n < 1:
        raise ValueError("n must be a positive integer.")

    result = 0
    for k in range(1, n + 1):
        result += (1 / k) - (1 / (k + 1))

    return result

def main():
    print("Telescoping Sum Solver")
    print("This program computes the value of P(n) defined as a telescoping sum.")

    try:
        # Input n
        n = int(input("Enter a positive integer (n): "))

        if n < 1:
            print("Error: n must be a positive integer.")
            return

        # Compute the result
        result = calculate_p(n)

        # Display the result
        print("The value of P(" + str(n) + ") is:", result)

    except ValueError:
        print("Error: Please enter a valid positive integer for n.")

if __name__ == "__main__":
    main()
