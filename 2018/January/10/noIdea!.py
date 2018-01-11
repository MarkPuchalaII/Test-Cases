# This challenge's lesson was reading instructions
# I didn't read that n might have repeating values
# So I kept getting errors when I tried to compute n as a set
# running n as a list solved this.
# However I could no longer run n.intersection(a)-n.intersection(b)
# I used a solution I got from the discussion section.
# It used a summation to quickly find (n in a) - (n in b)

    # My spaghetti code version
N,M = input().split()
n = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))     # Pretty clever how the summation is made
r = sum((i in a) - (i in b) for i in n)# using true == 1 & false == 0
print(r)

################################################################################

    # My more refined version
N,M = input().split()
n,a,b = list(map(int, input().split())) , set(map(int, input().split())) , set(map(int, input().split()))
print(sum((i in a) - (i in b) for i in n))

################################################################################

    # Hackerrank's approach
    They... Didn't have an approach?
