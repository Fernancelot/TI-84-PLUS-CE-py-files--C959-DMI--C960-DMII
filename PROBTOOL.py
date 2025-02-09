# UNIT 5: Probability Tools
# Purpose:
# This program includes three sections to handle:
# 1. Conditional Probability and Bayes' Theorem.
# 2. Combinatorial Probability.
# 3. Probability Distributions.

# Function to calculate factorial (used in combinations)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Function to calculate combinations: C(n, r) = n! / (r! * (n - r)!)
def combinations(n, r):
    if r > n or r < 0:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

# Section 1: Conditional Probability and Bayes' Theorem
def conditional_probability():
    print("\nConditional Probability and Bayes' Theorem")
    try:
        P_A = float(input("Enter P(A) (probability of A): "))
        P_B = float(input("Enter P(B) (probability of B): "))
        P_B_given_A = float(input("Enter P(B|A) (probability of B given A): "))

        # Calculate P(A|B) using Bayes' Theorem: P(A|B) = P(B|A) * P(A) / P(B)
        P_A_given_B = (P_B_given_A * P_A) / P_B
        print("P(A|B):", round(P_A_given_B, 4))
    except ValueError:
        print("Error: Please enter valid probabilities.")
    except ZeroDivisionError:
        print("Error: P(B) cannot be zero.")

# Section 2: Combinatorial Probability
def combinatorial_probability():
    print("\nCombinatorial Probability")
    try:
        total_outcomes = int(input("Enter the total number of outcomes (n): "))
        desired_outcomes = int(input("Enter the desired number of outcomes (r): "))
        sample_size = int(input("Enter the sample size (k): "))

        # Calculate probabilities based on combinations
        numerator = combinations(desired_outcomes, sample_size) * combinations(total_outcomes - desired_outcomes, sample_size - sample_size)
        denominator = combinations(total_outcomes, sample_size)

        probability = numerator / denominator
        print("Probability:", round(probability, 4))
    except ValueError:
        print("Error: Please enter valid integers.")
    except ZeroDivisionError:
        print("Error: Denominator cannot be zero.")

# Section 3: Probability Distributions
def probability_distributions():
    print("\nProbability Distributions")
    try:
        outcomes = list(map(int, input("Enter the outcomes (comma-separated): ").split(',')))
        probabilities = list(map(float, input("Enter the probabilities for each outcome (comma-separated): ").split(',')))

        if len(outcomes) != len(probabilities):
            print("Error: The number of outcomes and probabilities must match.")
            return
        if not all(0 <= p <= 1 for p in probabilities) or sum(probabilities) != 1:
            print("Error: Probabilities must be between 0 and 1, and their sum must equal 1.")
            return

        # Display the probability distribution
        print("Outcome \t Probability")
        for outcome, prob in zip(outcomes, probabilities):
            print(outcome, "\t", round(prob, 4))

        # Calculate expected value
        expected_value = sum(outcome * prob for outcome, prob in zip(outcomes, probabilities))
        print("Expected Value:", round(expected_value, 4))
    except ValueError:
        print("Error: Please enter valid numbers.")

def main():
    while True:
        print("\nUNIT 5: Probability Tools")
        print("1. Conditional Probability and Bayes' Theorem")
        print("2. Combinatorial Probability")
        print("3. Probability Distributions")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            conditional_probability()
        elif choice == '2':
            combinatorial_probability()
        elif choice == '3':
            probability_distributions()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()
