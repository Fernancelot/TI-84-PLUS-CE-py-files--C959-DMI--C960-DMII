# STARNBAR.py: Star-and-Bar Multiset Calculator
# Purpose:
# This program solves problems involving the distribution of indistinguishable objects
# into distinguishable bins using the "star-and-bar" method. It computes the number of ways
# to place n objects into m bins.

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

# Function to calculate star-and-bar result
def star_and_bar(objects, bins):
    # Formula: C(n + m - 1, m - 1)
    return combinations(objects + bins - 1, bins - 1)

def main():
    print("Star-and-Bar Multiset Calculator")
    print("This program calculates the number of ways to distribute n indistinguishable objects into m distinguishable bins.")

    try:
        # Input number of objects and bins
        objects = int(input("Enter the number of objects (n): "))
        bins = int(input("Enter the number of bins (m): "))

        if objects < 0 or bins <= 0:
            print("Error: Number of objects must be non-negative, and number of bins must be positive.")
            return

        # Calculate and display the result
        result = star_and_bar(objects, bins)
        print("The number of ways to distribute " + str(objects) + " objects into " + str(bins) + " bins is: " + str(result))
    
    except ValueError:
        print("Error: Please enter valid integers for objects and bins.")

if __name__ == "__main__":
    main()
