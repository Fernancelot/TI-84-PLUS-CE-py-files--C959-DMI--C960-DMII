# UNIT 2: MODULE 4: Division Algorithm
# Purpose:
# This program demonstrates the Division Algorithm. It calculates the quotient
# and remainder when dividing two integers and simplifies the results using
# modular arithmetic.

# Usage and Instructions:
# - Input two integers: the base value (x) and divisor (y).
# - The program calculates and displays:
#   - The modular simplifications of x and y.
#   - The result of modular arithmetic.

def calculate_div_and_mod():
    try:
        x = int(input("Enter the base value for x, or, enter 0 to quit: "))
        if x == 0:
            return False
        x_exp = int(input("Enter the exponent for x (enter 1 if there is no exponent): "))
        y = int(input("Enter the base value for y: "))
        y_exp = int(input("Enter the exponent for y (enter 1 if there is no exponent): "))
    except:
        print("Invalid input. Please enter integers only.")
        return True

    x_mod = x % 10
    y_mod = y % 10
    x_mod_exp = (x_mod ** x_exp) % 10
    y_mod_exp = (y_mod ** y_exp) % 10
    result = (x_mod_exp + y_mod_exp) % 10

    print("(" + str(x) + "^" + str(x_exp) + " + " + str(y) + "^" + str(y_exp) + ") mod 10 = [(" +
          str(x) + " mod 10)^" + str(x_exp) + " + (" + str(y) + " mod 10)^" + str(y_exp) + "] mod 10")
    print("= [(" + str(x_mod) + "^" + str(x_exp) + " mod 10) + (" + str(y_mod) + "^" + str(y_exp) +
          " mod 10)] mod 10")
    print("= [" + str(x_mod_exp) + " + " + str(y_mod_exp) + "] mod 10 = " + str(result))
    return True

def main():
    while calculate_div_and_mod():
        pass

main()
