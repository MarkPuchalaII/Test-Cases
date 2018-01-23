# This challenge's lesson: combinations() takes two parameters
# Use len(list(thing)) to count the length of anything without its own len()

    # My spaghetti code version
from itertools import combinations
n = int(input())
a = input().split()
k = int(input())
n , d = 0 , 0
for i in combinations(a, k):
  if 'a' in i: n += 1
  d +=1
print(n/d)


################################################################################

    # My refined version
from itertools import combinations
n , a , k = int(input()) , input().split() , int(input())
n , d = 0 , len(list(combinations(a,k)))
for i in combinations(a, k) : n += 'a' in i
print(n/d)

################################################################################

    # Hackerrank's approach
from itertools import combinations 

N = int(input())
S = raw_input().split(' ')
K = int(input())

num = 0
den = 0

for c in combinations(S,K):
    den+=1
    num+='a' in c
    
print float(num)/den
