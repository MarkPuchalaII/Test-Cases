# This challenge's lesson was the | operator. 
# I like it better than s.union()
# That is all.

    # My spaghetti code version

e, e, f, f = input(), set(map(int, input().split())), input(), set(map(int, input().split()))
print(len(e | f))

################################################################################

    # My more refined version

e, e, f, f = input(), set(map(int, input().split())), input(), set(map(int, input().split()))
print(len(e | f))  # Looks like my spaghetti was as good as my refined! WOOHOO!

################################################################################

    # Hackerrank's approach
E = int(raw_input())
English = set(raw_input().split())

F = int(raw_input())
French = set(raw_input().split())

print len(English | French) # Basically the same thing.
