# This challenge's lesson: Sometimes *[_ for _ in range] is better than [_ for _ in range]
# Though maybe it's not. Still, I like this "a, b, in input()". I'm gonna test that out more.

    # My spaghetti code version
from itertools import groupby
print(*[(len(list(b)), int(a)) for a, b in groupby(input())])

################################################################################

    # My refined version
from itertools import groupby
[print((len(list(b)), int(a)), end = " ") for a, b in groupby(input())]

################################################################################

    # Hackerrank's approach
from __future__ import print_function
from itertools import *

for i,j in groupby(map(int,list(raw_input()))):
    print(tuple([len(list(j)), i]) ,end = " ")
