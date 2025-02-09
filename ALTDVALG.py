# UNIT 2: Modular Arithmetic Enhancements
# Purpose:
# This program performs modular arithmetic, including division, addition,
# multiplication, and modular exponentiation.

def division_algorithm(x, y):
    div = x // y
    mod = x % y
    return div, mod

def modular_addition(x, y, n):
    return (x + y) % n

def modular_multiplication(x, y, n):
    return (x * y) % n

def modular_exponentiation(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def main():
    print("Modular Arithmetic Program")
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    mod = int(input("Enter modulo n: "))
    
    div, mod_result = division_algorithm(x, y)
    print("x div y: " + str(div))
    print("x mod y: " + str(mod_result))
    
    add_result = modular_addition(x, y, mod)
    print("Modular addition (x + y) mod n: " + str(add_result))
    
    mult_result = modular_multiplication(x, y, mod)
    print("Modular multiplication (x * y) mod n: " + str(mult_result))
    
    exp_result = modular_exponentiation(x, y, mod)
    print("Modular exponentiation (x^y) mod n: " + str(exp_result))

main()
