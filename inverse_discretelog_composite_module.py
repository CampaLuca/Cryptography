from sage.all import *

####### Finding the inverse module a composite number (a^x = y (mod p1*p2*p3*...)) ########
###### It works if a is coprime with the module
def inverse(primes, value):
    values = [pow(value,-1,p) for p in primes]
    return crt(values,primes)

###### Find the discrete logarithm module a composite number (it works if the base and the module are coprime) #######
def dis_log_composite_module2(primes, value, base):
    values = []
    for p in primes:
        k = Mod(value, p)
        values.append(k.log(base))
    
    primes_minus_one = [p-1 for p in primes]
    return crt(values, primes_minus_one)

# TEST
"""base = 5
module = 1781
exponent = 24
val = pow(base, exponent, module)
print(f'The dis log is : {dis_log_composite_module2([13, 137], val, base)}')"""


####### How to constraint the values withing groups or rings
"""R = IntegerModRing(m)
G = GF(b)
g_a = G(a)


x1 = int(G(r-b)/G(pow(a,y,m)))
y1 = log_b(G(r-b)/R(x1), g_a)
"""
# In this way we can perform divisions and logarithms without computing inverses. It is done automatically


