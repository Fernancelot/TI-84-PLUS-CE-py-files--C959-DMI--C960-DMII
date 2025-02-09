# UNIT 4: Inclusion-Exclusion Principle
# Purpose:
# This program calculates the union of two or three sets using the inclusion-exclusion principle.

def inclusion_exclusion_two(A, B, AB):
    return A + B - AB

def inclusion_exclusion_three(A, B, C, AB, AC, BC, ABC):
    return A + B + C - AB - AC - BC + ABC

def main():
    print("Inclusion-Exclusion Principle Calculator")
    choice = int(input("Enter 2 for two sets, 3 for three sets: "))
    if choice == 2:
        try:
            A = int(input("Enter |A|: "))
            B = int(input("Enter |B|: "))
            AB = int(input("Enter |A ∩ B|: "))
            union = inclusion_exclusion_two(A, B, AB)
            print("|A ∪ B| =", union)
        except ValueError:
            print("Error: Please enter valid integers.")
    elif choice == 3:
        try:
            A = int(input("Enter |A|: "))
            B = int(input("Enter |B|: "))
            C = int(input("Enter |C|: "))
            AB = int(input("Enter |A ∩ B|: "))
            AC = int(input("Enter |A ∩ C|: "))
            BC = int(input("Enter |B ∩ C|: "))
            ABC = int(input("Enter |A ∩ B ∩ C|: "))
            union = inclusion_exclusion_three(A, B, C, AB, AC, BC, ABC)
            print("|A ∪ B ∪ C| =", union)
        except ValueError:
            print("Error: Please enter valid integers.")
    else:
        print("Invalid choice. Please select 2 or 3.")

main()
