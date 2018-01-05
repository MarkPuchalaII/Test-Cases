# This one wasnt very difficult at all... I just followed the instructions.
# Not much to do here, really.

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

################################################################################

    # Hackerrank's approach
    
import textwrap
S = raw_input()
w = input()
print textwrap.fill(S,w)

    # Their problem solvers clearly don't follow the format I'm given. Odd.
