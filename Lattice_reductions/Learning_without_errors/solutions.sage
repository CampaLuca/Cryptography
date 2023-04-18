couples = [ ([30, 7, 25], 11), ([2, 16, 16], 8), ([2, 4, 4], 1), ([9, 25, 9], 28)]   # ( a_i, <a_i, s>)

A = matrix(GF(31), [couple[0] for couple in couples])
b = matrix(GF(31), [couple[1] for couple in couples]).transpose()
print((A.solve_right(b)).transpose())
