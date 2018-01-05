# A little trial and error to understand..
# Ended up solving it with the following hash table: 

# If N = 7 , M = 21
#  row1(3, 1, 3)
#  row2(2, 3, 2)
#  row3(1, 5, 1)
#  row4(2, W, 2)
#  row5(1, 5, 1)
#  row6(2, 3, 2)
#  row7(3, 1, 3)

N, M = map(int,input().split()) 
for i in range(1,N,2): 
    print ("---"*int((N-i)/2)+".|."*i+"---"*int((N-i)/2))
print("---"*int((N-2)/2)+"-WELCOME-"+"---"*int((N-2)/2))
for i in range(N-2,-1,-2): 
    print("---"*int((N-i)/2)+".|."*i+"---"*int((N-i)/2))

################################################################################

    # Hackerrank's approach
    # Python String center() Method
 
    # Syntax
    # str.center(width[, fillchar])
    # width: Total width of the string.
    # fillchar: Filler character.
    
N,M = map(int,raw_input().split())
for i in xrange(1, N, 2): 
    print ( str('.|.')*i ).center(M, '-') # Their code is much simpler than mine
print str('WELCOME').center(M, '-')       # I didn't realize str.center() works this way
for i in xrange(N-2, -1, -2): 
    print ( str('.|.')*i ).center(M, '-')
