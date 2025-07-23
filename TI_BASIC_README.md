# TI-BASIC Versions of TI-Python Programs

This document describes the TI-BASIC versions (.8xp files) that have been created from the original TI-Python programs. These programs maintain the same user interface and functionality while being adapted for the TI-BASIC programming environment.

## Completed TI-BASIC Programs

### Mathematical Utilities
- **BSCPROB.8xp** - Basic Probability Calculator
  - Calculates probability given event outcomes and total outcomes
  - Includes input validation for non-negative values
  
- **PERMCOMB.8xp** - Permutations and Combinations Calculator
  - Menu-driven interface for choosing P(n,r) or C(n,r)
  - Uses built-in factorial function for efficiency
  - Validates that 0 ≤ r ≤ n

- **EXPCTVAL.8xp** - Expected Value Calculator
  - Calculates expected value for discrete random variables
  - Supports up to 10 values for TI-BASIC list limitations
  - Validates probabilities sum to 1

### Base and Number Theory
- **BASEBCNV.8xp** - Base Conversion Program
  - Converts numbers between bases 2-10
  - Validates input digits are valid for source base
  - Uses string manipulation for output formatting

- **EXTDEUCL.8xp** - Extended Euclidean Algorithm
  - Calculates GCD and finds coefficients x, y for ax + by = gcd(a,b)
  - Determines if multiplicative inverse exists
  - Shows step-by-step coefficient calculation

### Cryptography
- **RSAALGR.8xp** - RSA Algorithm Implementation
  - Complete RSA encryption/decryption
  - Includes GCD checking for public exponent validation
  - Modular inverse calculation using Extended Euclidean Algorithm
  - Modular exponentiation for encryption/decryption

### Advanced Probability
- **PROBTOOL.8xp** - Probability Tools Suite
  - Menu system with 4 options:
    1. Conditional Probability and Bayes' Theorem
    2. Combinatorial Probability
    3. Probability Distributions (up to 5 outcomes)
    4. Exit
  - Comprehensive input validation and error handling

## Key Adaptations Made for TI-BASIC

### Syntax Changes
- `print()` → `Disp`
- `input()` → `Input "PROMPT:",VAR`
- String concatenation using `+` operator
- `While` loops with explicit `End` statements
- `If/Then/Else/End` structure for conditionals

### Data Structure Adaptations
- Python lists → TI-BASIC lists (L1, L2, etc.)
- Limited to 10 elements for practical memory usage
- String handling using `Str1`, `sub()`, and string concatenation

### Mathematical Functions
- `//` (integer division) → `int(A/B)`
- `%` (modulo) → `remainder(A,B)`
- `**` (exponentiation) → `^` or repeated multiplication
- Factorial using built-in `!` operator

### User Interface Preservation
- Same menu structures and option numbering
- Identical input prompts and output formatting
- Consistent error messages and validation
- Clear program titles and descriptions

## Installation Instructions

1. Transfer .8xp files to TI-84 Plus CE using TI-Connect CE software
2. Programs appear in PRGM menu under the same names
3. Run programs using `prgm` menu selection
4. All programs are standalone - no dependencies required

## Memory Considerations

- TI-BASIC programs use calculator RAM
- Each program is optimized for minimal memory usage
- Archive programs to Flash memory if needed for space
- Programs can be run from Archive (may be slightly slower)

## Compatibility

- Designed for TI-84 Plus CE family calculators
- Compatible with TI-OS 5.3.0 and higher
- Uses standard TI-BASIC commands - no special apps required

## Future Enhancements

Additional programs from the Python collection will be converted following the same patterns and user interface principles established in these initial conversions.