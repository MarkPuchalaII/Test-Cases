# This challenge's lesson was optimizing my for-loops
# They wanted me to practice the set.add() function,
# but I determined it to be useless for this exercise
# I feel like set.add() should be used after the set's initialization
# I don't see why I'd use it during...

    # My spaghetti code version
n = int(input())
s = set()
for i in range(n) : 
  s.add(input())
print(len(s))

################################################################################

    # My more refined version
print(len(set(input() for i in range((int(input())))))) # So many parentheses...

################################################################################

    # Hackerrank's approach
stamps = set()
for _ in range(int(raw_input())):
    stamps.add(raw_input().strip())
print len(stamps)
