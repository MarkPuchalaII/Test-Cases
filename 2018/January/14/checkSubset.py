# This challenge's lesson: There's  more than one way to find an answer
# I think my answer is more readable
# but the refinement I found is clever, and thus worth noting.

    # My spaghetti code version

for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a, a, b, b = int(input()), set(input().split()) , int(input()), set(input().split()) 
    print(b | a == b)

################################################################################

    # My refined version

for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a, a, b, b = int(input()), set(input().split()) , int(input()), set(input().split()) 
    print(not bool(a-b))

    # After studying Hackerrank's approach
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a, a, b, b = int(input()), set(input().split()) , int(input()), set(input().split()) 
    print(a <= b)

################################################################################

    # Hackerrank's approach
for i in range(int(raw_input())): 
    a = int(raw_input()); A = set(raw_input().split()); 
    b = int(raw_input()); B = set(raw_input().split());
    print A <= B
