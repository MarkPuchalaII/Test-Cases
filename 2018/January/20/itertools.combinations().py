# This challenge's lesson: Be careful of your ranges. 
# It's easy to put the wrong numbers, and make a broken loop.

    # My spaghetti code version
from itertools import combinations
a , b = input().split()
for i in range(1,int(b)+1) : [print(''.join(j)) for j in combinations(sorted(a), i)]

################################################################################

    # My refined version
from itertools import combinations
a , b = input().split()
for i in range(1,int(b)+1) : [print(''.join(j)) for j in combinations(sorted(a), i)]

################################################################################

    # Hackerrank's approach

from itertools import combinations
S,k = raw_input().split()
for j in range(1,int(k)+1):
    for i in combinations(sorted(S),j):
        print "".join(i)
