# This challenge's lesson was the - operator. 
# I like it better than s.difference()
# Why didn't they include all of these in one lesson? -.-

    # My spaghetti code version

e, e, f, f = input(), set(map(int, input().split())), input(), set(map(int, input().split()))
print(len(e - f))

################################################################################

    # My more refined version

e, e, f, f = input(), set(map(int, input().split())), input(), set(map(int, input().split()))
print(len(e - f))  # Looks like my spaghetti was as good as my refined! WOOHOO!

################################################################################

    # Hackerrank's approach
E = int(raw_input()) 
English = set(raw_input().split())
# STEP 1 - Store the space separated input of roll numbers as sets with variables English and French. 
F = int(raw_input())
French = set(raw_input().split())
# STEP 2 - Print the length of the differences between the sets English and French.
print len(English - French) # Basically the same thing.
