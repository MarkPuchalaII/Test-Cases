# This challenge's lesson: ABSOLUTELY NOTHING
# I got this from someone else's code.
# I don't actually understand it, either!

# I guess cmath.polar() returns the modulus & the phase of a complex number?

    # My spaghetti code version
import cmath
print(*cmath.polar(complex(input())), sep='\n')

################################################################################

    # My refined version
import cmath
print(*cmath.polar(complex(input())), sep='\n')

    # After futher study
import cmath
print(*cmath.polar(complex(input())), sep='\n')

################################################################################

    # Hackerrank's approach
from cmath import polar
polar = polar(complex(raw_input()))
print polar[0]
print polar[1]
