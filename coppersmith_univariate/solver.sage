from sage.all import *

def create_matrix(N, eq, X):
    ll = []
    

    

    a = eq.coefficients(sparse=False)

    d = eq.degree()
    #epsilon = min(1/d, 0.18)
    h = ceil((((1/0.18))+1)/d)
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
                l.append(0)

            temp_eq = eq^j
            new_coeff = temp_eq.coefficients(sparse=False)
            precomputed = pow(N, h-1-j)*pow(X,i)
            for exponent in range(len(new_coeff)):
                l.append(new_coeff[exponent]*precomputed*pow(X, exponent))
            G.append(l)
    
    max_length = 0
    for l in G:
        if len(l) > max_length:
            max_length = len(l)
    
    G.sort(key = len)

    for l in G:
        if len(l) < max_length:
            for v in range(max_length-len(l)):
                l.append(0)

    for l in G:
        print(l)
    
    

    print(G)
    m = Matrix(G)
    print(m)

    

    M = m.LLL()
    print()
    print(M)
    print()


    #Q = M[0][0] + M[0][1]*x + M[0][2]*x^2 + M[0][3]*x^3 + M[0][4]*x^4 + M[0][5]*x^5 + M[0][6]*x^6 + M[0][7]*x^7 + M[0][8]*x^8
    for k in range(1):
        Q = 0
        for p in range(d*h):
            Q += (M[k][p]//(X^p))*x^p
        #Q = M[k][0] + M[k][1]*x + M[k][2]*x^2 + M[k][3]*x^3 + M[k][4]*x^4 + M[k][5]*x^5 + M[k][6]*x^6 + M[k][7]*x^7 + M[k][8]*x^8

        print(Q.roots(ring=ZZ))
    

#K = Zmod(10001)
#P.<x> = PolynomialRing(K, implementation='NTL')
R.<x> = PolynomialRing(ZZ)

# N = 4611686047418417197
# eq = 1942528644709637042 + 1234567890123456789*x + 987654321987654321*x^2 + x^3
# X = 2^14
N = 10001
eq = -222 + 5000*x + 10*x^2 + x^3
X = 10


create_matrix(N, eq, X)