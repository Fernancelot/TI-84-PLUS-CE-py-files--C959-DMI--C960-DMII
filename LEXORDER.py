# Lexicographic Order Generator
# Purpose:
# This program takes a set of alphanumeric characters as input and generates all permutations
# in lexicographic order, displaying 5 lines at a time.

from itertools import permutations

# Function to generate and display lexicographic permutations with breaks
def generate_lexicographic_order(chars):
    sorted_chars = sorted(chars)
    all_permutations = ["".join(perm) for perm in permutations(sorted_chars)]
    return all_permutations

def display_with_breaks(permutations, break_size):
    for i in range(0, len(permutations), break_size):
        chunk = permutations[i:i+break_size]
        for perm in chunk:
            print(perm)
        if i + break_size < len(permutations):
            input("Press Enter to continue...")

def main():
    print("Lexicographic Order Generator")
    print("This program generates all permutations of a given set of characters in lexicographic order.")

    try:
        # Input the set of characters
        chars = input("Enter the set of characters (e.g., abcde): ").strip()

        if not chars:
            print("Error: Please provide a non-empty set of characters.")
            return

        # Generate lexicographic permutations
        permutations = generate_lexicographic_order(chars)

        # Display the results with breaks
        print("\nLexicographic Order (5 lines at a time):")
        display_with_breaks(permutations, 5)

    except Exception as e:
        print("Error:", e)
        print("Please check your inputs and try again.")

if __name__ == "__main__":
    main()
