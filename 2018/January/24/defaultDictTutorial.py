# This challenge's lesson: print(this or that) is beautiful!!
# Also, keep track of where you put "i = input()" in a loop.
# You might not need it.
# Finally, calling a collection seems to work like calling  list.
# For example, if you "map(function, collection)"
# It's much like saying "map(function, [x1,x2,x3])"

    # My spaghetti code version
from collections import defaultdict
n , m = map( int , input().split())
d = defaultdict(list)
for i in range(n):
  d[input()].append(i+1)
for _ in range(m):
  i = input()
  if i in d : print(" ".join(map(str, d[i])))
  else : print(-1)


################################################################################

    # My refined version
from collections import defaultdict
n , m = map(int , input().split())
d = defaultdict(list)

for i in range(n) : d[input()].append(i+1)
for _ in range(m) : print(" ".join(map(str, d[input()])) or -1)


################################################################################

    # Hackerrank's approach

    # They didn't have an editorial for this one
