# RSA Algorithm for TI-Python

# Function to compute the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find the modular inverse of e mod phi using the Extended Euclidean Algorithm
def modular_inverse(e, phi):
    a, b, u, v = phi, e, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        u, v = v, u - q * v
    if a == 1:
        return u % phi
    return None  # No modular inverse exists

# Function to compute (base^exp) % mod efficiently
def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

def main():
    print("RSA Algorithm for TI-Python")

    # Input primes p and q
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    e = int(input("Enter public exponent e: "))

    # Calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)

    # Check if gcd(e, phi) == 1
    if gcd(e, phi) != 1:
        print("Invalid public exponent e. It must be coprime with phi(n).")
        return

    # Calculate private key d
    d = modular_inverse(e, phi)
    if d is None:
        print("Failed to find modular inverse of e.")
        return

    print("Public key: (e =", e, ", n =", n, ")")
    print("Private key: (d =", d, ", n =", n, ")")

    # Encrypt plaintext
    plaintext = int(input("Enter plaintext (as integer): "))
    ciphertext = modular_exponentiation(plaintext, e, n)
    print("Ciphertext:", ciphertext)

    # Decrypt ciphertext
    decrypted_text = modular_exponentiation(ciphertext, d, n)
    print("Decrypted text:", decrypted_text)

main()






