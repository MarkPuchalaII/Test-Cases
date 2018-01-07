# I did NOT like my attempt for this one.
# I had to fumble around a LOT to get the right answer

def print_formatted(n):
    l = len(str(bin(n)))-1
    for i in range(1,n+1) :
      print(str(i).rjust(l-1) +
            str(oct(i)[2:]).rjust(l) +
            str(  "%X" % i).rjust(l) +
            str(bin(i)[2:]).rjust(l))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

################################################################################

def fun(N):
    width = len(bin(N)) - 2
    for i in range(1,N+1):
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width)

n = input()
fun(n)
