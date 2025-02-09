# UNIT 2: RSA Encryption
# Purpose:
# This program computes RSA keys, encrypts messages, and decrypts ciphertexts.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modular_inverse(e, phi):
    t, new_t = 0, 1
    r, new_r = phi, e
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None
    if t < 0:
        t += phi
    return t

def rsa_encrypt(message, e, n):
    return pow(message, e, n)

def rsa_decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

def main():
    print("RSA Encryption Program")
    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))
    n = p * q
    phi = (p - 1) * (q - 1)
    print("n = " + str(n) + ", phi = " + str(phi))

    e = int(input("Enter public exponent e (1 < e < phi, gcd(e, phi) = 1): "))
    if gcd(e, phi) != 1:
        print("e and phi are not coprime. Please try again.")
        return

    d = modular_inverse(e, phi)
    if d is None:
        print("Modular inverse not found. Please try again.")
        return

    print("Private key (d): " + str(d))

    message = int(input("Enter message to encrypt (as an integer): "))
    ciphertext = rsa_encrypt(message, e, n)
    print("Ciphertext: " + str(ciphertext))

    decrypted_message = rsa_decrypt(ciphertext, d, n)
    print("Decrypted message: " + str(decrypted_message))

main()
