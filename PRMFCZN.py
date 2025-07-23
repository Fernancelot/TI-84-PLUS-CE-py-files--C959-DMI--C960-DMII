# UNIT 2: MODULE 5: Prime Factorization
# Purpose:
# This program determines if a number is prime. If it is not, the program computes
# the prime factorization of the number.

# Usage and Instructions:
# - Enter a positive integer when prompted.
# - The program will:
#   1. Check if the number is prime.
#   2. If not, compute and display its prime factorization.

def is_prime(n):
    # Determines if a number is prime.
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # Divisible by 2 or 3
    i = 5
    while i * i <= n:  # Check divisors up to √n
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    # Computes the prime factorization of n.
    i = 2
    factors = []
    while i * i <= n:  # Check divisors up to √n
        if n % i:  # If not divisible by i, try the next number
            i += 1
        else:  # If divisible by i, divide and record i as a factor
            n //= i
            factors.append(i)
    if n > 1:  # If n is a prime number greater than 1, add it to the factors
        factors.append(n)
    return factors

def main():
    print("Prime Factorization Program")
    print("Determine if a number is prime, and if not, find its prime factors.")
    
    try:
        num = int(input("Enter a number: "))
        if is_prime(num):
            print(str(num) + " is a PRIME number")
        else:
            print(str(num) + " is NOT a PRIME number")
            print("Prime factorization:", prime_factors(num))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

main()






