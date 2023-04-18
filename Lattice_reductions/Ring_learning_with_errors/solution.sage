from sage.all import *

def ring_learning_with_errors(p, irreducible_polynomial, couples, error_bound):

    Z = Zmod(p)
    S = PolynomialRing(Z,'x')
    R = S.quotient(irreducible_polynomial, 'x')
    error_coefficients = []

    for i in range(-error_bound, error_bound+1):
        for j in range(-error_bound, error_bound+1):
            error_coefficients.append((i,j))

    for u_0, v_0 in error_coefficients:
        for u_1, v_1 in error_coefficients:
            A = matrix(R, [couple[0] for couple in couples[:2]])
            b = matrix(R, [couples[0][1]+u_0*x+v_0, couples[1][1]+u_1*x+v_1])
            
            try:
                temp_solution = (A.solve_left(b))
                print(temp_solution)
                found = True
                for lista in couples:
                    eq = vector(Matrix(R, [lista[1]])) - vector(Matrix(R, [lista[0]])*temp_solution[0])
                    for e in eq:
                        for coeff in list(e):
                            if ((coeff > error_bound and (c - Matrix(ZZ,a)*temp_solution) < (p-error_bound))):
                                found = False
                                break
                if found:
                    return temp_solution
                
            except:
                continue


ring_learning_with_errors(211, x^2+3*x+7, [[23*x + 188, 34*x + 183], [129*x + 1, 48*x + 158], [89*x + 47, 64*x + 10]], 2)