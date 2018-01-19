# This challenge's lesson: *parameter in .format() functions.
# I also need to verse myself more to use .format in general.

    # My spaghetti code version
a , b = int(input()) , int(input())
print(str(a//b)+"\n"+str(a%b)+"\n"+str(divmod(a,b)))

################################################################################

    # My refined version
print('{0}\n{1}\n({0}, {1})'.format(*divmod(int(input()), int(input()))))
# Got this from someone else's code

################################################################################

    # Hackerrank's approach
a = int(raw_input())
b = int(raw_input())
print a/b
print a%b
print divmod(a,b)
