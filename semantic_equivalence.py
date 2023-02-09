from z3 import *

x, y = BitVecs('x y', 64)

# First formula
f1 = x ^ y

# Second formula
f2 = x - y - 2 * (~x | y) - 2

# Creating a solver
s = Solver()

# Asserting that the two formulas are equivalent
s.add(f1 == f2)

# Checking if the assertions are satisfiable
if s.check() == sat:
    print("The two formulas are semantically equivalent.")
else:
    print("The two formulas are not semantically equivalent.")
