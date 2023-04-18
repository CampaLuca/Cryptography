def agcd_iterative(values, error_bound, agcd_lower_bound):
    for error in range(error_bound+1):
        comparison = 1
        for e in range(error_bound+1):
            comparison = (values[1] - e)
            temp_g = gcd(values[0] - error, comparison)
            if temp_g > agcd_lower_bound:
                found = True
                for val in values:
                    if ((val % temp_g) > error_bound):
                        found = False
                        break
                if found:
                    return temp_g


def agcd_lattice_reduction(values, error_bound, agcd_lower_bound):
    matrix = []
    
    first_row = [error_bound]
    for val in values[1:]:
        first_row.append(val)
    matrix.append(first_row)

    for i in range(len(values)-1):
        r = [0]
        for j in range(len(values)-1):
            if i == j:
                r.append(-values[0])
            else:
                r.append(0)
    
        matrix.append(r)

    M = Matrix(ZZ, matrix)
    M = M.LLL()

    # k_0 * error_bound
    k_0 = abs(M[0][0]) // error_bound
    e_0 = values[0] % k_0
    g_0 = (values[0] - e_0) // k_0

    # test

    found = True
    for val in values:
        if ((val % g_0) > error_bound):
            found = False
            break
    if found:
        return g_0

    

values = [406612341, 552092054, 475395575, 538700529]
error_bound = 256
agcd_lower_bound = 2^19
print(agcd_iterative(values, error_bound, agcd_lower_bound))
print(agcd_lattice_reduction(values, error_bound, agcd_lower_bound))

values = [779830132241441617767717, 849824224537324100834415, 769124183710968506661470]
error_bound = 2^20
agcd_lower_bound = 2^44-1
print(agcd_lattice_reduction(values, error_bound, agcd_lower_bound))

