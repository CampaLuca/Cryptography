from sage.all import *
import sys, getopt
import random

# indexes of primorial numbers whos value + 1 is smooth prim
indexes = [0,1,2,3,4,5,11,75,171,172,384,457,616,643,1391, 1613,2122,2647,2673,4413,13494,31260,33237]
P = Primes() # list of primes

def get_gcd_primorial_prime(p, gcd_v, min_width=None, max_width=None):
    for j in range(500):
        q = 2
        for i in range(j,10000):
            q *= P[i]

            if gcd(q,p-1) == gcd_v and is_prime(q+1):
                goodness = True
                if min_width and q.nbits() < min_width:
                    goodness = False
                if max_width and q.nbits() > max_width:
                    goodness = False
                
                if goodness:
                    q += 1
                    return q
                
                

def get_known_smooth_prime(min_width=None, max_width=None):
    if min_width == None and max_width == None:
        prime = sloane.A002110[random.choice(indexes)]+1
        return prime

    for index in indexes:
        prime = sloane.A002110[index]+1
        
        goodness = True
        if min_width != None and prime.nbits() < min_width:
            goodness = False
        if max_width != None and prime.nbits() > max_width:
            goodness = False
        
        if goodness:
            return prime
    
    
    return get_gcd_primorial_prime(2, 1, min_width=min_width, max_width=max_width)


def generate(n, gcd=None, min_width=None, max_width=None):
    if gcd != None:
        if n != 2:
            print("Wrong parameters: gcd requires n=2")
            return None
        
        p1 = get_known_smooth_prime(min_width=min_width, max_width=max_width)
        p2 = get_gcd_primorial_prime(p1, gcd, min_width, max_width)
        return [p1, p1]
    else:
        p = get_known_smooth_prime(min_width=min_width, max_width=max_width)
        return [p]
        
            

def main(argv):

    if not argv:
        print ("""
                python generator.py <options>

                OPTIONS:
                --min_width: minimum bit size for the primes
                --max_width: maximum bit size for the primes
                --n: number of primes to be generated 0 < n <= 2
                --gcd: gcd between primorial numbers (if n == 2)
            """)
        sys.exit(0)
    opts, args = getopt.getopt(argv, "hi:o:",["n=","min_width=", "max_width=", "gcd="])

    min_width = None
    max_width = None
    n = 1
    gcd = None

    for opt, arg in opts:
        if opt == '-h':
            print ("""
                python generator.py <options>

                OPTIONS:
                --min_width: minimum bit size for the primes
                --max_width: maximum bit size for the primes
                --n: number of primes to be generated 0 < n <= 2
                --gcd: gcd between primorial numbers (if n == 2)
            """)
            sys.exit()
        elif opt in ("--min_width"):
            min_width = int(arg)
        elif opt in ("--max_width"):
            max_width = int(arg)
        elif opt in ("--n"):
            n = int(arg)
        elif opt in ("--gcd"):
            gcd = int(arg)

    print(generate(n, gcd=gcd, min_width=min_width, max_width=max_width))



if __name__ == "__main__":
   main(sys.argv[1:])