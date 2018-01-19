# This challenge's lesson: I don't ALWAYS prefer operators over functions

    # My spaghetti code version
a , b , c , d = int(input()) , int(input()) , int(input()) , int(input())
print(pow(a,b) + pow(c,d))

    # ALSO WORKS!
    print(a**b + c**d)

################################################################################

    # My refined version
print(pow(int(input()) , int(input())) + pow(int(input()) , int(input())))

################################################################################

    # Hackerrank's approach
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
d = int(raw_input())

print a**b + c**d
