from z3 import *

def check_python(s, l):
    v = 0
    for i in range(l):
        if s[i] == "-":
            v -= 1
        elif s[i] == "*":
            v *= 2
        else:
            return 0
    return v % (2 ** 64) == 0xffffffffbadc0de0

def check_sat(solver, input_str):
    v = BitVec("v", 64)
    solver.add(v == 0)
    for i in range(len(input_str)):
        c = input_str[i]
        solver.push()
        solver.add(c == ord("-"))
        if solver.check() == sat:
            solver.pop()
            solver.push()
            solver.add(c == ord("*"))
            if solver.check() == sat:
                solver.pop()
                solver.add(Or(c == ord("-"), c == ord("*")))
                solver.add(v == v * 2)
            else:
                solver.pop()
                solver.add(c == ord("-"))
                solver.add(v == v - 1)
        else:
            solver.pop()
            return unsat
    solver.add(v == 0xffffffffbadc0de0)
    return solver.check()

solver = Solver()
length = 8 # you can adjust the length to get a shorter string
input_str = [BitVec("s" + str(i), 8) for i in range(length)]
for i in range(length):
    solver.add(input_str[i] >= ord("-"), input_str[i] <= ord("*"))

if check_sat(solver, input_str) == sat:
    model = solver.model()
    s = "".join(map(chr, [model[c].as_long() for c in input_str]))
    l = len(s)
    assert check_python(s, l)
    print(s, l)
else:
    print("unsat")
