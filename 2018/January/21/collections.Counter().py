# This challenge's lesson: Nothing yet
# Coming back to this tomorrow

    # My spaghetti code version
from collections import Counter
x = int(input())
s = Counter(list(map(int,input().split())))
n = int(input())

t = 0
for _ in range(n) :
  i = input().split()
  if s[int(i[0])] :
    s[int(i[0])] -= 1
    t += int(i[1])
print(t)


################################################################################

    # My refined version


################################################################################

    # Hackerrank's approach
from collections import Counter
X = input()
S = Counter(map(int,raw_input().split()))
N = input()
earnings = 0
for customer in range(N):
    size, x_i = map(int,raw_input().split())
    if size in S and S[size] > 0:
        S[size] -= 1
        earnings += x_i
            
print earnings 
