# I didn't solve this originally
# I instead reverse-engineered someone else's code.
# So I'm now more familiar with advanced techniques
# using teh following functions: str.center(), str.join()

import string
a = string.ascii_lowercase

def print_rangoli(n):
    l = []
    for i in range(n):
        s = "-".join(a[i:n])
        l.append((s[:0:-1]+s).center(4*n-3,"-"))  # I optimized the code, here.
    print("\n".join(l[:0:-1]+l))                  # Both my array calls use the same technique.
                                                  # The code I learned from didn't do this.
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

################################################################################

    # The code I learned from
    
import string                                      # He imported the string library.
alpha = string.ascii_lowercase                     # so he could use ascii_lowercase
                                                   #
def print_rangoli(n):                              # Make a function
  L = []                                           # that creates an array
  for i in range(n):                               # and stores a string in that array n times
      s = "-".join(alpha[i:n])                     # (if n == 5) a-b-c-d-e, b-c-d-e, c-d-e, d-e, e
      L.append((s[::-1]+s[1:]).center(4*n-3, "-")) # Then added that to the end of the L array.
  print('\n'.join(L[:0:-1]+L))                     # Print the list in reverse, EXCEPT the last line.
                                                   # Then print the list in order.
                                                   # Pretty clever, dude.

################################################################################

# Hackerrank's approach
                                                            # So here's my dissection of their methods....
n = int(input())                                            # They take n on an input
for i in range(n):                                          # Then prepare to print lines that many times
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))   # They then made strings with - between each letter
    print((s+s[::-1][1:]).center(n*4-3, '-'))               # And centered that string, surrounded by -
                                                            # Exactly enough - to fill in the blanks...
for i in range(n-1):                                        #
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1)) # After that, they ran the same thing, just in reverse.
    print((s+s[::-1][1:]).center(n*4-3, '-'))               # This is going to take a few more studies to fully comprehend.
