from z3 import *

def is_semantically_equivalent(f1, f2):
    solver = Solver()
    solver.add(f1 == f2)
    return solver.check() == sat

x = BitVec("x", 64)

# Formula 1: the transformation suggested
f1 = x & BitVecVal(2**32-1, 64)
f1 = Extract(31, 0, ZeroExt(32, f1))

# Formula 2: the expected behavior
f2 = Extract(31, 0, ZeroExt(32, x))

# Prove semantic equivalence
assert(is_semantically_equivalent(f1, f2))
