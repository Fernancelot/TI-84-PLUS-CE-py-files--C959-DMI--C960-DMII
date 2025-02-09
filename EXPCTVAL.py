# UNIT 5: Expected Value
# Purpose:
# This program calculates the expected value of a discrete random variable.

def expected_value(values, probabilities):
    return sum(v * p for v, p in zip(values, probabilities))

def main():
    print("Expected Value Calculator")
    try:
        values = list(map(float, input("Enter values (comma-separated): ").split(',')))
        probabilities = list(map(float, input("Enter probabilities (comma-separated): ").split(',')))
        if len(values) != len(probabilities):
            print("Error: Number of values must match number of probabilities.")
            return
        if not all(0 <= p <= 1 for p in probabilities) or sum(probabilities) != 1:
            print("Error: Probabilities must be between 0 and 1 and sum to 1.")
            return

        result = expected_value(values, probabilities)
        print("Expected Value = " + str(result))
    except ValueError:
        print("Error: Please enter valid numbers.")

main()
