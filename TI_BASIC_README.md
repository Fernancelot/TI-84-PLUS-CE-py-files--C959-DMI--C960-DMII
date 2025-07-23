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

- **INCLEXCL.8xp** - Inclusion-Exclusion Principle Calculator
  - Calculates union of 2 or 3 sets using inclusion-exclusion
  - Menu-driven selection for number of sets
  - Clear step-by-step input prompts

- **STARNBAR.8xp** - Star-and-Bar Multiset Calculator
  - Calculates ways to distribute n objects into m bins
  - Uses combinatorial formula C(n+m-1, m-1)
  - Input validation for non-negative objects and positive bins

- **TSUMSLVR.8xp** - Telescoping Sum Solver
  - Computes P(n) for telescoping sum series
  - Formula: sum(k=1 to n)[1/k - 1/(k+1)]
  - Handles positive integer validation

### Base and Number Theory
- **BASEBCNV.8xp** - Base Conversion Program
  - Converts numbers between bases 2-10
  - Validates input digits are valid for source base
  - Uses string manipulation for output formatting

- **EXTDEUCL.8xp** - Extended Euclidean Algorithm
  - Calculates GCD and finds coefficients x, y for ax + by = gcd(a,b)
  - Determines if multiplicative inverse exists
  - Shows step-by-step coefficient calculation

- **STDEUCLD.8xp** - Standard Euclidean Algorithm
  - Calculates GCD showing each division step
  - Displays step-by-step calculation process
  - Clear formula presentation for each step

- **PRMFCZN.8xp** - Prime Factorization Program
  - Determines if number is prime
  - If not prime, finds complete prime factorization
  - Optimized primality testing algorithm

- **FSTMDEXP.8xp** - Fast Modular Exponentiation
  - Efficient modular exponentiation using successive squaring
  - Handles large exponents efficiently
  - Used in cryptographic applications

- **MDLRINVR.8xp** - Modular Inverse Calculator
  - Finds modular multiplicative inverse (assumes prime modulus)
  - Uses Fermat's Little Theorem: a^(p-2) mod p
  - Includes GCD checking for validity

- **DIVSALGR.8xp** - Division Algorithm Demo
  - Demonstrates modular arithmetic properties
  - Shows step-by-step simplification process
  - Repeatable calculations with loop structure

- **EQVLEXPR.8xp** - Exponent Decomposer
  - Decomposes exponents into powers of 2
  - Shows equivalent expressions for efficient computation
  - Useful for understanding binary exponentiation

- **SEQNCMOD.8xp** - Sequence Modulo Solver
  - Computes recursive sequence based on mod 3 rules
  - Handles different cases for remainders 0, 1, 2
  - Iterative calculation up to target term

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

### Reference Charts
- **BIGOGROW.8xp** - Big O Notation Reference
  - Growth rate comparison from O(1) to O(n!)
  - Algorithm complexity reference for common algorithms
  - Searching and sorting algorithm summaries

- **BIN2HEX.8xp** - Binary to Hexadecimal Reference
  - Conversion chart for binary/hex/decimal
  - Reference for values 0-15
  - Useful for computer science applications

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

Additional programs from the Python collection can be converted following the same patterns and user interface principles established in these conversions. The remaining programs include:

- ALTBASEB.py, ALTDVALG.py, ALTRSAD.py, ALTRSAE.py - Alternative algorithm implementations
- CNGRMDLN.py - Congruence modulo calculations  
- DBHCONV.py - Database/hash conversions
- FSMSIML.py - Finite state machine simulations
- LEXORDER.py - Lexicographic ordering (complex for TI-BASIC)
- LOOPALZR.py - Loop analysis tools
- MDEXPNTS.py - Modular exponent calculations
- RCURRLN2.py, RCURRLTN.py - Recurrence relation solvers
- RSANOTES.py - RSA algorithm notes
- U6STVLDN.py - Unit 6 study validation

**Current Status: 20 of 33 programs converted (60% complete)**

Each remaining program will maintain the same design principles:
- Preserve original user interface and menu structure
- Maintain mathematical accuracy and algorithm efficiency  
- Include comprehensive input validation and error handling
- Optimize for TI-84 Plus CE memory and display constraints