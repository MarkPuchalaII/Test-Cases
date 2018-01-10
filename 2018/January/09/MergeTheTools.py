# Figured this all out researching two things:
# First: collections.OrderedDict.fromkeys()
# next : a neat loop, s[i:i+k] for i in range(0,len(s),k)

from collections import OrderedDict
def merge_the_tools(string, k):
    for t in range(0,len(string),k) :                       # Iterate over each substring of length k
        print("".join(OrderedDict.fromkeys(string[t:t+k]))) # Remove all duplicate characters AND PRINT!
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

####

    # Hackerrank's approach

s = input()                       # HAHA LOOK AT THIS JARBLED MESS
k = int(input())                  # My code is WAY more elegant! <3
num_subsegments = int(len(s) / k) # Though I must admit their version is much more readable...

for index in range(num_subsegments):
    # Subsegment string
    t = s[index * k : (index + 1) * k]
    
    # Subsequence string having distinct characters
    u = ""
    
    # If a character is not already in 'u', append
    for c in t:
        if c not in u:
            u += c

    # Print final converted string
    print(u)
