# This challenge's lesson: Use other peopes' code to finish the job quick!
# This is now outdated. The new version is in Test-Cases/2018/January/22

    # My spaghetti code version
from itertools import combinations

N = int(input())
L = input().split()
K = int(input())

C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)
print("{0:.3}".format(len(list(F))/len(C)))

################################################################################

    # My refined version
from itertools import combinations 
N, S, K = int(input()) , input().split(' ') , int(input())
num , den = 0 , 0
for c in combinations(S,K):
    den+=1
    num+='a' in c
print(float(num)/den)

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
