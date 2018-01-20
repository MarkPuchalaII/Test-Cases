# This challenge's lesson: Remember * can be an iterator.
# Turns out Hackerrank's approach was virtually identical to my spahgetti approach.
# I guess I am improving!

    # My spaghetti code version

from itertools import product
a , b = list(input().split()) , list(input().split())
for i in product(map(int,a), map(int,b)) : print(i, end = " ")

################################################################################

    # My refined version
print(*product(map(int,list(input().split())), map(int,list(input().split()))))

################################################################################

    # Hackerrank's approach

from itertools import product

A = map(int,input().split())
B = map(int,input().split())

for item in product(A,B):
    print(item,end=' ')
