# This challenge's lesson: Hackerrank is obsolete. I need a better challenge.

    # My spaghetti code version
from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))

################################################################################

    # My refined version
from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))

################################################################################

    # Hackerrank's approach
from itertools import *

K, M = map(int, raw_input().split())
N = []

for _ in xrange(K):
     N.append(map(int, raw_input().split())[1:])        
MAX = -1
for i in product(*N):
    MAX = max(sum(map(lambda x: x**2, i))%M, MAX)
    
print MAX  
