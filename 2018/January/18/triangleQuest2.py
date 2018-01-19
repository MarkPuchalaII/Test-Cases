# This challenge's lesson: The value of time
# Always consider a brute-force.
# Sure, it might not be the most clever way,
# but sometimes it just might be the fastest

    # My spaghetti code version
for i in range(0,int(input())):
  print([1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321, 
            123456787654321, 12345678987654321,   12345678910987654321][i])

################################################################################

    # My refined version
for i in range(1,int(input())+1): print((10**i//9)**2)

    # After futher study
    # It stayed the same

################################################################################

    # Hackerrank's approach
for i in xrange(1,int(raw_input())+1):
    print (10**i/9)**2

# Another Method 01:
for i in range(1,int(raw_input())+1):
    print  reduce(lambda x, y: x + (10 ** (y - 1)), range(1, i + 1))**2

# Another Method 02:
for i in range(1,int(raw_input())+1):
    print [1, 121, 12321, 1234321, 123454321, 12345654321,1234567654321, 123456787654321, 12345678987654321][i-1]
