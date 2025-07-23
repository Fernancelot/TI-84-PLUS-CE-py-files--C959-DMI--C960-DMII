# Modular Exponentiation

# EXAMPLE: 2b. 15^26 mod 7
# 2b. 15^26 mod 7 = (15 mod 7)26 mod 7 = (1)26 mod 7 = 1 mod 7 = 1

# Calculate 15^26 mod 7.
# Use modular exponentiation (repeatedly squaring base & taking result modulo 7)

# Start with the base, 15:
# 15 mod 7 = 1
# Square the base:
# 15^2 mod 7 = 1
# Continue squaring and taking the modulo 7:
# 15^4 mod 7 = 1
# 15^8 mod 7 = 1
# 15^16 mod 7 = 1
# Now, we can use the fact that 26 = 16 + 8 + 2.
# So, 15^26 mod 7 = (15^16 * 15^8 * 15^2) mod 7
# = (1 * 1 * 1) mod 7
# = 1
# Therefore, the result of 15^26 mod 7 is 1.







