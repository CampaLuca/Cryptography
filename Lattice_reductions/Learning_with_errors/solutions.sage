def learning_with_errors_easy(error_bound, p, couples):
    for error_1 in range(-error_bound, error_bound+1, +1):
        for error_2 in range(-error_bound, error_bound+1, +1):
            A = matrix(GF(p), [couple[0] for couple in couples[:2]])
            b = matrix(GF(p), [couples[0][1]+error_1, couples[1][1]+error_2]).transpose()
            
            try:
                temp_solution = (A.solve_right(b))
                found = True
                for a, c in couples:
                    if ((c - Matrix(ZZ,a)*temp_solution) > error_bound and (c - Matrix(ZZ,a)*temp_solution) < (p-error_bound)):
                        found = False
                        break
                if found:
                    return temp_solution
            except:
                continue

couples = [ ([7, 19], 152), ([14, 1], 126), ([8, 20], 205), ([18, 9], 122)]   # ( a_i, <a_i, s>)
p = 211
error_bound = 3

print(learning_with_errors_easy(error_bound, p, couples))