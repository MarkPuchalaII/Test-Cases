# This challenge's lesson: "array of commands" is a thing

    # My spaghetti code version
from itertools import permutations
a , b = input().split()
[print(''.join(i)) for i in permutations(sorted(a), int(b))]

################################################################################

    # My refined version
from itertools import permutations
a , b = input().split()
[print(''.join(i)) for i in permutations(sorted(a), int(b))]

################################################################################

    # Hackerrank's approach

from itertools import *
S, k = raw_input().split()
for i in permutations(sorted(S),int(k)):
    print("".join(i))
