# This challenge's lesson: Reference
# I don't always have to know the answer
# I can piece something together from the code of others
# Learning form experience may not be precise,
# But it seems to lead to a greater vision.
# I may feel nervous that I'm "cheapshotting this",
# But this might just pay off in the end. 
# So I'm going to try it more.


    # My spaghetti code version
import math 
AB , BC = int(input()) , int(input()) 
tan = math.degrees(math.atan2(AB,BC))
print(str(int(round(tan)))+'°')

################################################################################

    # My refined version
import math 
AB , BC = int(input()) , int(input()) 
print(str(int(round(math.degrees(math.atan2(AB,BC)))))+'°')

    # After futher study
from math import *
print(str(int(round(degrees(math.atan2(int(input()),int(input()))))))+'°')

################################################################################

    # Hackerrank's approach
from math import *
print "%.0f°" % degrees(atan2(float(raw_input()), float(raw_input())))
