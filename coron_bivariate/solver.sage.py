

# This file was *autogenerated* from the file ../coron_bivariate/solver.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_0p18 = RealNumber('0.18'); _sage_const_0 = Integer(0); _sage_const_5 = Integer(5); _sage_const_2 = Integer(2); _sage_const_131 = Integer(131); _sage_const_1400 = Integer(1400); _sage_const_20 = Integer(20); _sage_const_1286 = Integer(1286); _sage_const_4 = Integer(4); _sage_const_30 = Integer(30)
from sage.all import *

def coppersmith_univariate(N, eq, X):
    ll = []
    a = eq.coefficients(sparse=False)

    d = eq.degree()
    #epsilon = min(1/d, 0.18)
    h = ceil((((_sage_const_1 /_sage_const_0p18 ))+_sage_const_1 )/d)
    #h = 3
    print(f'Degree: {d}')
    #print(f'Epsilon: {epsilon}')
    print(f'h: {h}')

    # bound if not given
    #X = 2^15

    G = []
    for i in range(d):
        for j in range(h):
            l = []

            for _ in range(i):
                l.append(_sage_const_0 )

            temp_eq = eq**j
            new_coeff = temp_eq.coefficients(sparse=False)
            precomputed = pow(N, h-_sage_const_1 -j)*pow(X,i)
            for exponent in range(len(new_coeff)):
                l.append(new_coeff[exponent]*precomputed*pow(X, exponent))
            G.append(l)
    
    max_length = _sage_const_0 
    for l in G:
        if len(l) > max_length:
            max_length = len(l)
    
    G.sort(key = len)

    for l in G:
        if len(l) < max_length:
            for v in range(max_length-len(l)):
                l.append(_sage_const_0 )

    for l in G:
        print(l)
    
    

    print(G)
    m = Matrix(G)
    print(m)

    

    M = m.LLL()

    solutions = []
    for k in range(_sage_const_1 ):
        Q = _sage_const_0 
        for p in range(d*h):
            Q += (M[k][p]//(X**p))*x**p

        solutions.append(Q.roots(ring=ZZ))

    return solutions
    

# #K = Zmod(10001)
# #P.<x> = PolynomialRing(K, implementation='NTL')
# R.<x> = PolynomialRing(ZZ)

# # N = 4611686047418417197
# # eq = 1942528644709637042 + 1234567890123456789*x + 987654321987654321*x^2 + x^3
# # X = 2^14
# N = 10001
# eq = -222 + 5000*x + 10*x^2 + x^3
# X = 10


# coppersmith_univariate(N, eq, X)

def number_of_leading_zeros(lista):
    count = _sage_const_0 
    for el in lista:
        if el == _sage_const_0 :
            count += _sage_const_1 
        else:
            break
    return count


def coron_method_bivariate_equations(N, eq, X, Y):

    total_degree = eq.degree()
    x_degree = eq.degree(x)
    y_degree = eq.degree(y)

    degree = max(x_degree, y_degree)


    degree_of_each_var = eq.degrees()
    variables = eq.variables()

    # k should be able to generate all the monomials of eq and others, at least 2.
    k = randint(degree+_sage_const_1 , degree+_sage_const_5 )

    # generate all the (d+k)^2 monomials
    print(k)
    # compute k^2 polynomials
    polys = []
    for a in range(k):
        for b in range(k):
            polys.append(x**a*y**b*eq)
    
    # fix i0 and j0
    i0 = randint(_sage_const_1 ,degree)
    j0 = i0

    # choose k^2 monomials
    monomials = []
    for i in range(k):
        for j in range(k):
            monomials.append(x**(i0+i)*y**(j0+j))

    monomials.sort(key=lambda x: x.degree(), reverse=True)

    other_monomials = []
    for i in range(degree+k):
        for j in range(degree+k):
            if not x**(i)*y**(j) in monomials:
                other_monomials.append(x**(i)*y**(j))

    other_monomials.sort(key=lambda x: x.degree(), reverse=True)

    print(monomials)

    matrix_list = []

    

    for poly in polys:
        ll = []
        for monomial in monomials:
            ll.append( poly.coefficient({x:monomial.degree(x), y:monomial.degree(y)}))
        matrix_list.append(ll)

    temp_matrix = Matrix(matrix_list)
    N = temp_matrix.determinant()

    for index in range(len(polys)):
        for monomial in other_monomials:
            matrix_list[index].append( polys[index].coefficient({x:monomial.degree(x), y:monomial.degree(y)}) )
    


    matrix_list.sort(key=lambda x: number_of_leading_zeros(x))

    
    for i in range((degree+k)**_sage_const_2 ):
        ll = []
        for j in range((degree+k)**_sage_const_2 ):
            if i == j:
                ll.append(N)
            else:
                ll.append(_sage_const_0 )
        matrix_list.append(ll)
    print(matrix_list)
    M = Matrix(ZZ, matrix_list)

    
    M = M.hermite_form()
    
    new_M = M[[x+k**_sage_const_2  for x in range((degree+k)**_sage_const_2 -k**_sage_const_2 )], [x+k**_sage_const_2  for x in range((degree+k)**_sage_const_2 -k**_sage_const_2 )]]

    temp_M = []

    for i in range((degree+k)**_sage_const_2 -k**_sage_const_2 ):
        ll = []
        for j in range((degree+k)**_sage_const_2 -k**_sage_const_2 ):
            ll.append( X**(other_monomials[j].degree(x))*Y**(other_monomials[j].degree(y))*new_M[i][j])
        temp_M.append(ll)

    M = Matrix(ZZ, temp_M)
    M = M.LLL()

    print(M)
    eq_reduced = _sage_const_0 
    for i in range(len(other_monomials)):
        eq_reduced += (M[_sage_const_0 ][i]//(X**(other_monomials[i].degree(x))*Y**(other_monomials[i].degree(y))))*other_monomials[i]

    print(eq_reduced)

    Q = eq.resultant(eq_reduced, y)
    
    solutions = []
    for val, exp in (Q.univariate_polynomial()).roots(ring=ZZ):
        y_values = (eq(val, y).univariate_polynomial()).roots(ring=ZZ)
        for y_val, exp in y_values:
            solutions.append((val, y_val))

    return solutions

a = _sage_const_131  # 127
b = -_sage_const_1400  # -1207
c = _sage_const_20  # -1461
d = -_sage_const_1286  # 21
N = _sage_const_131 **_sage_const_4 
X = _sage_const_30 
Y = _sage_const_20 
R = PolynomialRing(ZZ, names=('x', 'y',)); (x, y,) = R._first_ngens(2)
eq = a*x*y + b*x + c*y + d
#eq = x^2*y + x*y^2 + 1
sol = coron_method_bivariate_equations(N, eq, X, Y)
print(sol)

