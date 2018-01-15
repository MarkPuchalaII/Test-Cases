# This challenge's lesson: 

    # My spaghetti code version
a = set(map(int, input().split()))
b = True
for i in range(int(input())) : 
  n = set(map(int, input().split()))
  if len(n-a) > 0 : 
    b = False
    break
print(b) 

################################################################################

    # My refined version
a = set(input().split())
print(all(map(lambda x: (a > x), [set(input().split()) for _ in range(int(input()))])))

    # After futher study


################################################################################

    # Hackerrank's approach
A = set(raw_input().split()); # Theirs was the best possible version far as I can tell
print all(map(lambda x: (A > x), [set(raw_input().split()) for i in range(int(raw_input()))])) 
