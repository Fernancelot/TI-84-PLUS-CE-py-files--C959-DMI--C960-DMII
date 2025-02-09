# UNIT 1: MODULE 2: Order of Growth Notes
# Purpose:
# This note explains the growth order of functions and their impact on execution speed.
# The functions are ranked from slowest to fastest growth (shortest to longest runtime).
# This ranking helps analyze the efficiency of algorithms.

# Functions Ranked by Growth:
# (a) log10(n) - Slowest growth, fastest execution
# (b) n * log(n)
# (c) n^2
# (d) n^10
# (e) 10^n - Fastest growth, slowest execution

# Execution Speed:
# Faster algorithms grow slower (e.g., log(n)), while slower algorithms grow faster (e.g., 10^n).
# Constant functions (e.g., O(1)) are faster than logarithmic ones, but not listed here as they do not scale with input size.

# Usage Tip:
# When designing algorithms, aim for functions with slower growth rates like log(n) or n * log(n).
