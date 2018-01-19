# This challenge's lesson: You won't always have the best answer
# Doesn't mean you can't submit the one you do have, though.

    # My spaghetti code version
a , b , m = int(input()) , int(input()) , int(input())
print("{0}\n{1}".format(*[pow(a,b),pow(a,b,m)]))

################################################################################

    # My refined version
a , b , m = int(input()) , int(input()) , int(input())
print("{0}\n{1}".format(*[pow(a,b),pow(a,b,m)]))
# I feel like there's a way to get this down to one line
# But I don't yet know of one for this specific case.

################################################################################

    # Hackerrank's approach
a = int(raw_input())
b = int(raw_input())
m = int(raw_input())
print a**b
print pow(a,b,m)
