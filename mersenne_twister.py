from sage.all import *
from randcrack import RandCrack 

# it is used to crack mersenne twister
# mersenne twister works on 32 bits and aggregate those values in order to generate bigger values. For
# example, in order to create a random value of 128 bits, it generates (getrandbits) 4 values of 32 bits and shift them to the left


### Example: how to use RandCrack
"""
rc = RandCrack() 

for i in range(len(cts)):
    r = "valore"
    x1 = seed
    y1 = log_b(G(r-b)/R(x1), g_a)

    y2 = seed
    x2 = int(G(r-b)/G(pow(a,y,m)))


    x = min(x1,x2)
    y = min(y1,y2)

    # exploit the fact that tthe random generator generates values greater than 32 bits by shifiting more generated values of 32 bits

    val = x

    for j in range(512 // 32):
        rc.submit(val % 2**32)
        val = val >> 32

    val = y

    if i < 19:
        for j in range(512//32):
            rc.submit(val % 2**32)
            val = val >> 32
    else:
        rand = rc.predict_getrandbits(512)
        assert(rand == y)
"""







