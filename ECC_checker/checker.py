from sage.all import *
from cysignals.alarm import alarm, AlarmInterrupt, cancel_alarm
import sys, getopt

def check_pohlig_hellman(E,p):
    factorization = None
    if not is_prime(E.order()):
        try:
            alarm(20)        
            factorization = factor(E.order())        
        except (AlarmInterrupt,KeyboardInterrupt):      
            return
        else:
            print(f"The factorization of the order is: {factorization}")
            print("Is it a smooth integer?")
            print("[+] By manually checking the factors, maybe it is vulnerable to Pohlig-Hellman attack\n")
            cancel_alarm()


def check_smart_attack(E,p):
    if p == E.order() or E.trace_of_frobenius() == 1:
        print("[+] Vulnerable to SMART ATTACK\n")
    return 

def check_mov_attack(E,p):
    # check for supersingular curve
    P = E.random_point()
    if E.order() == p+1 or (p-1)*P == 0 or (p+1)*P == 0:
        print("[+] Vulnerable to MOV attack (Supersingular Curve)\n")
        return

    G = E.gens()[0]
    # computing embedding degree
    embedding_degree = 0
    for k in range(1,300):
        if p**k % G.order() == 1:
            embedding_degree = k
            break 

    if (embedding_degree > 0):
        print("[+] Vulnerable to MOV attack by using Weil Pairings\n")
    
    return

def check_pollard_speedup(E,p):
    if E.discriminant() < (1<<90):
        print("Pollard's Rho algorithm can be used tbanks to the possible speed up\n")

    return


def check_twist(E,p):
    if E.j_invariant() == 1728:
        print("[+] Quartic Twist is possible\n")
    
    if E.j_invariant() == 0:
        print("[+] Cubic Twist\n")

def check_curve(a,b,p):
    E = EllipticCurve(GF(p), [a,b])

    check_pohlig_hellman(E, p)
    check_smart_attack(E, p)
    check_mov_attack(E, p)
    check_pollard_speedup(E,p)
    check_twist(E,p)

def main(argv):

    if not argv:
        print ("""
                python generator.py <options>

                OPTIONS:
                --a: minimum bit size for the primes
                --b: maximum bit size for the primes
                --p: number of primes to be generated 0 < n <= 2
            """)
        sys.exit(0)
    opts, args = getopt.getopt(argv, "hi:o:",["a=","b=", "p="])

    a = None
    b = None
    p = None

    for opt, arg in opts:
        if opt == '-h':
            print ("""
                python generator.py <options>

                OPTIONS:
                --a: minimum bit size for the primes
                --b: maximum bit size for the primes
                --p: number of primes to be generated 0 < n <= 2
            """)
            sys.exit()
        elif opt in ("--a"):
            if arg[:2] == '0x':
                a = int(arg, 16)
            elif arg[:2] == '0b':
                a = int(arg, 2)
            else:
                a = int(arg)
        elif opt in ("--b"):
            if arg[:2] == '0x':
                b = int(arg, 16)
            elif arg[:2] == '0b':
                b = int(arg, 2)
            else:
                b = int(arg)
        elif opt in ("--p"):
            if arg[:2] == '0x':
                p = int(arg, 16)
            elif arg[:2] == '0b':
                p = int(arg, 2)
            else:
                p = int(arg)

    if not p and not a and not b:
        print("All the parameters are required!")
        sys.exit(0)

    check_curve(a,b,p)



if __name__ == "__main__":
   main(sys.argv[1:])