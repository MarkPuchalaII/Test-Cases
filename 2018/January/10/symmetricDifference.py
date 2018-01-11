# I'm going to take a new approach to my coding challenges
# first, some spaghetti code
# second a refined approach
# Sometimes I will make a third attempt 
#     based on what I learn after Hackerrank's approach
# But we'll see

# This challenge's lesson was the ^ operator, for symmetric differences.

n = input()
a = set(map(int, input().split()))     # My spaghetti code version
n = input()
b = set(map(int, input().split()))
c = b.difference(a)
c.update(a.difference(b))
for e in sorted(c):
    print(e)

################################################################################

n = input() ; a = set(map(int, input().split()))  # My more refined version
n = input() ; b = set(map(int, input().split()))
c = a ^ b 
for e in sorted(c): print(e)

################################################################################

 # Enter your code here. Read input from STDIN. Print output to STDOU
M = raw_input();m = raw_input().split()
N = raw_input();n = raw_input().split()

print "\n".join(sorted(list(set(m) ^ set(n)),key=int))
