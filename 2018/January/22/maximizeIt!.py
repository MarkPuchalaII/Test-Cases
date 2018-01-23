# This challenge's lesson: map(lambda) is very useful
# product(*x) is also very useful
# So much to absorb on this one... Wow, was it a challenge.

    # My spaghetti code version
from itertools import product
k, m = map(int, input().split())
n = [list(map(int, input().split()))[1:] for _ in range(k)]

mx = -1
for i in product(*n):
     k = sum(map(lambda x : x**2, i))%m
     mx = max(k, mx) 
print(mx)


################################################################################

    # My refined version
from itertools import product
k, m = map(int, input().split())
n = [list(map(int, input().split()))[1:] for _ in range(k)] 
print(max([sum(map(lambda x : x**2, i))%m for i in product(*n)]))

################################################################################

    # Hackerrank's approach
from itertools import * #

K, M = map(int, raw_input().split()) #
N = []

for _ in xrange(K):
     N.append(map(int, raw_input().split())[1:])
MAX = -1
for i in product(*N):
    MAX = max(sum(map(lambda x: x**2, i))%M, MAX)

print MAX

N = (list(map(int, input().split()))[1:]
print(N)



