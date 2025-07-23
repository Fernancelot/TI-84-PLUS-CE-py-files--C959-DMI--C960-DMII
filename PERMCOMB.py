# UNIT 4: Permutations and Combinations
# Purpose:
# This program calculates permutations (P(n, r)) and combinations (C(n, r)).

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def permutations(n, r):
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def main():
    print("Permutations and Combinations Calculator")
    print("1: Calculate Permutations (P(n, r))")
    print("2: Calculate Combinations (C(n, r))")
    
    choice = int(input("Enter your choice (1 or 2): "))
    if choice not in [1, 2]:
        print("Invalid choice. Please select 1 or 2.")
        return

    try:
        n = int(input("Enter n (total items): "))
        r = int(input("Enter r (items chosen): "))
        if n < 0 or r < 0 or r > n:
            print("Error: Ensure 0 <= r <= n.")
            return
    except ValueError:
        print("Error: Please enter valid integers for n and r.")
        return

    if choice == 1:
        result = permutations(n, r)
        print("P(" + str(n) + ", " + str(r) + ") = " + str(result))
    elif choice == 2:
        result = combinations(n, r)
        print("C(" + str(n) + ", " + str(r) + ") = " + str(result))

main()







