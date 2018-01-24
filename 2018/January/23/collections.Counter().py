# This challenge's lesson: re-read your code before you debug it
# It'll help you maintain awareness. Don't always do this, though.
# Sometimes, just blindly running things can free mental space
# thus speeding up the process, or at least streamlining it for you.

    # My spaghetti code version
from collections import Counter
x , x = int(input()), Counter(list(map(int, input().split())))
n = int(input())

t = 0
for i in range(1,n+1):
  j = list(map(int, input().split()))
  if x[j[0]] :
    x[j[0]] -= 1
    t += j[1]

print(t)


################################################################################

    # My refined version
from collections import Counter
x , x = int(input()) , Counter(list(map(int, input().split())))
n , t = int(input()) , 0
for i in range(1,n+1):
  j = list(map(int, input().split()))
  if x[j[0]] :
    x[j[0]] -= 1
    t += j[1]
print(t)

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
