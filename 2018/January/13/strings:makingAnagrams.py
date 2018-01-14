# This challenge's lessons were with eval() and format().
# I'm warming up to the format() function a bit more,
# now that it's helping me with some more complex issues.
# I'm also learning some more clever ways to arrange my code
# So far I seem to be pushing for it to take up less space.
# I don't know if this is what I will want to maintain in the long run.

    # My spaghetti code version

def number_needed(a, b):
    q = a[:]
    for each in q : 
      if each in b: 
          a.remove(each)
          b.remove(each)
    return(len(a)+len(b))

a = sorted(list(input()))
b = sorted(list(input()))

print(number_needed(a, b))

################################################################################

    # My more refined version

def number_needed(a, b):
    for i in a[:] : 
      if i in b : 
          a.remove(i) , b.remove(i)
    return(len(a)+len(b))

a, b = sorted(list(input())) , sorted(list(input()))

print(number_needed(a, b))

################################################################################

    # Hackerrank's approach
from collections import *    
a = Counter(raw_input())
b = Counter(raw_input())
c = a - b
d = b - a
e = c + d                      # I have to admit I like their version better...
print len(list(e.elements()))
