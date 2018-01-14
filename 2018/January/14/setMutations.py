# This challenge's lesson was supposed to be update commands
# But my code didn't even use their operators.
# Because eval was simply better at the task
# Than writing down all the logic
# Anyway, intersction_update is   &= , update   is   |=
#         difference_update  is   -= , symmetric_difference_update is   ^=

    # My spaghetti code version

a,a = input(), set(map(int,input().split()))
n = int(input())
for i in range(n) : 
  n1 = input().split()
  n2 = set(map(int,input().split()))
  eval('a.{}({})'.format(n1[0],n2))
  
print(sum(a))

################################################################################

    # My refined version
a,a = input(), set(map(int,input().split()))
for i in range(int(input())) : 
  getattr(a , input().split()[0])(set(map(int , input().split()))) 
print(sum(a))

################################################################################

    # Hackerrank's approach
    
a = int(raw_input())
A = set(map(int, raw_input().split())) # STEP 1: Store the elements in set  in variable .
for i in range(int(raw_input())):
    s, b = raw_input().split() # STEP 2: Using loops & conditionals, execute the appropriate operations on set .
    if   s == 'intersection_update'        : A &= set(map(int, raw_input().split()))
    elif s == 'update'                     : A |= set(map(int, raw_input().split()))
    elif s == 'symmetric_difference_update': A ^= set(map(int, raw_input().split()))
    else                                   : A -= set(map(int, raw_input().split()))
print sum(A)  # STEP 3: Print the sum of .
