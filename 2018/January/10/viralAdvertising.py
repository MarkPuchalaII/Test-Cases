import sys, math

def viralAdvertising(n):        # This was my original version
    s ,m = 5, 0                 # I started with s, adding it into m
    for i in range(n):          # inevitably looping through that 
                                # Until I got the answer.
        m += math.floor(s/2)
        s = math.floor(s/2)* 3
    return(m)  

if __name__ == "__main__":         
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)   # 2, 5, 9, 15, 24...

################################################################################

import sys, math              # This is a placeholder for a more revised version
                              # I really think I can do this one better somehow.
def viralAdvertising(n):
    s = 5
    m = 0
    for i in range(n):
        #!/usr/bin/env python
        m += math.floor(s/2)
        s = math.floor(s/2)* 3
        print(m)

    return(m)  

if __name__ == "__main__":         # 2, 5, 9, 15, 24...
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
    
################################################################################

    # Hackerrank's approach
n = int(input())
shared = 5
total_opened = 0         # My code and Hackerrank's code were almost identical.

for _ in range(0, n):
    opened = int(shared / 2)
    total_opened += total_opened + opened
    shared = opened * 3
    
print(total_opened)
