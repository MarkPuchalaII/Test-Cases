# This challenge's lesson was the ^ operator. 
# I like it better than s.symmetric_difference()
# Please let this be the last one... Easy points is not my goal, here.

    # My spaghetti code version

e, e, f, f = input(), set(map(int, input().split())), input(), set(map(int, input().split()))
print(len(e ^ f))

################################################################################

    # My more refined version

e, e, f, f = input(), set(map(int, input().split())), input(), set(map(int, input().split()))
print(len(e ^ f))  # Looks like my spaghetti was as good as my refined! WOOHOO!

################################################################################

    # Hackerrank's approach
E = int(raw_input()) 
English = set(raw_input().split())
# STEP 1 - Store the space separated input of roll numbers as sets in variables English and French. 
F = int(raw_input())
French = set(raw_input().split())
# STEP 2 - Print the length of the symmetric difference of sets English and French.
print len(English ^ French) # Basically the same thing.
