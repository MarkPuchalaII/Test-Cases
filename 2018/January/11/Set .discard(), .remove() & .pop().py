# This challenge's lessons were with eval() and format().
# I'm warming up to the format() function a bit more,
# now that it's helping me with some more complex issues.
# I'm also learning some more clever ways to arrange my code
# So far I seem to be pushing for it to take up less space.
# I don't know if this is what I will want to maintain in the long run.

    # My spaghetti code version
n = int(input())
s = set(map(int, input().split()) for i in int(input()))
N = list(input() for i in range(int(input())))
for each in N :
  i = each.split()
  if i[0] == "pop" : s.pop()
  if i[0] == "remove" : s.remove(int(i[1]))
  if i[0] == "discard" : s.discard(int(i[1]))
print(sum(i for i in s)) # turns out sum(i for i in s) == sum(s). Neat!

    # I learned this from DeadMoroz.
n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))
print(sum(s))

################################################################################

    # My more refined version

n, s = int(input()) , set(map(int, input().split()))
for i in range(int(input())) : eval('s.{0}({1})'.format(*input().split()+['']))
print(sum(s))

################################################################################

    # Hackerrank's approach

n = int(raw_input()) # The approach is:
s = set([int(x) for x in raw_input().strip().split()]) # Step 1: Store the space separated input of elements in set .
for _ in range(int(raw_input())):                      # Step 2: Run a loop  times and store the commands in variable .

    a = list(raw_input().strip().split())

    if a[0] == 'pop':                                  # Step 3: Using conditionals, execute the appropriate commands on set .
        s.pop()
    elif a[0] == 'discard':
        s.discard(int(a[1]))
    else:
        s.remove(int(a[1]))

print sum(s)                                           # Step 4: Print the sum of set .
