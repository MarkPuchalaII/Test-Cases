# THis wasn't my code
# I just couldn't figure this one out
# I used someone else's code
# I've never seen ANY of these functions before
# How was I supposed to figure this out!???
import string
alpha = string.ascii_lowercase

def print_rangoli(n):
  L = []
  for i in range(n):
      s = "-".join(alpha[i:n])
      L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
  print('\n'.join(L[:0:-1]+L))
  
################################################################################

# Hackerrank's approach
                                                            # So here's my dissection of their methods....
n = int(input())                                        # They take n on an input
for i in range(n):                                          # Then prepare to print lines that many times
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))   # They then made strings with - between each letter 
    print((s+s[::-1][1:]).center(n*4-3, '-'))               # And centered that string, surrounded by -
                                                           # Exactly enough - to fill in the blanks...
for i in range(n-1):                                        # 
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1)) # After that, they ran the same thing, just in reverse.
    print((s+s[::-1][1:]).center(n*4-3, '-'))               # This is going to take a few more studies to fully comprehend.
