# This challenge's lesson: searching for elegant answers can waste valuable time

    # My spaghetti code version

for i in range(1,int(input())) : print(str(i)*i)
# So this didn't work because they wanted me printing ints, not strings.

################################################################################

    # My refined version

for i in range(1,int(input())) : print((10**i//9)*i)

################################################################################

    # Hackerrank's approach

for i in range(1,input()): 
    print  i * 10**i / 9
