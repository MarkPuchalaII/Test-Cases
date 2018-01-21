# This challenge's lesson: Nothing, really.
# Just practice. And I'd say I succeeded on that bit.

    # My spaghetti code version
from itertools import combinations_with_replacement
a , b = input().split()
[print(''.join(i)) for i in combinations_with_replacement(sorted(a),int(b))]

################################################################################

    # My refined version
from itertools import combinations_with_replacement
a , b = input().split()
[print(''.join(i)) for i in combinations_with_replacement(sorted(a),int(b))]

################################################################################

    # Hackerrank's approach
from itertools import combinations_with_replacement
S,k = raw_input().split()
for i in combinations_with_replacement(sorted(S),int(k)):
	print "".join(i)
