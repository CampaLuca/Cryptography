

# This file was *autogenerated* from the file Ring_learning_with_errors/solution.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_211 = Integer(211); _sage_const_3 = Integer(3); _sage_const_7 = Integer(7); _sage_const_23 = Integer(23); _sage_const_188 = Integer(188); _sage_const_34 = Integer(34); _sage_const_183 = Integer(183); _sage_const_129 = Integer(129); _sage_const_48 = Integer(48); _sage_const_158 = Integer(158); _sage_const_89 = Integer(89); _sage_const_47 = Integer(47); _sage_const_64 = Integer(64); _sage_const_10 = Integer(10)
from sage.all import *



def ring_learning_with_errors(p, irreducible_polynomial, couples, error_bound):

    Z = Zmod(p)
    S = PolynomialRing(Z,'x')
    R = S.quotient(irreducible_polynomial, 'x')
    error_coefficients = []

    for i in range(-error_bound, error_bound+_sage_const_1 ):
        for j in range(-error_bound, error_bound+_sage_const_1 ):
            error_coefficients.append((i,j))

    for u_0, v_0 in error_coefficients:
        for u_1, v_1 in error_coefficients:
            A = matrix(R, [couple[_sage_const_0 ] for couple in couples[:_sage_const_2 ]])
            b = matrix(R, [couples[_sage_const_0 ][_sage_const_1 ]+u_0*x+v_0, couples[_sage_const_1 ][_sage_const_1 ]+u_1*x+v_1])
            
            try:
                temp_solution = (A.solve_left(b))
                print(temp_solution)
                found = True
                for lista in couples:
                    eq = vector(Matrix(R, [lista[_sage_const_1 ]])) - vector(Matrix(R, [lista[_sage_const_0 ]])*temp_solution[_sage_const_0 ])
                    for e in eq:
                        for coeff in list(e):
                            if ((coeff > error_bound and (c - Matrix(ZZ,a)*temp_solution) < (p-error_bound))):
                                found = False
                                break
                if found:
                    return temp_solution
                
            except:
                continue


ring_learning_with_errors(_sage_const_211 , x**_sage_const_2 +_sage_const_3 *x+_sage_const_7 , [[_sage_const_23 *x + _sage_const_188 , _sage_const_34 *x + _sage_const_183 ], [_sage_const_129 *x + _sage_const_1 , _sage_const_48 *x + _sage_const_158 ], [_sage_const_89 *x + _sage_const_47 , _sage_const_64 *x + _sage_const_10 ]], _sage_const_2 )

