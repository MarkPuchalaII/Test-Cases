# This actually took longer than expected
def print_full_name(a, b): # So this was the one I finally got to work
    print("Hello {} {}! You just deleved into python.".format(a,b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

########################################################################

# And here was the Problem Tester's code
    print ("Hello %s %s! You just delved into python." % (a, b))      # Interestingly enough,
    print ("Hello " + a + " " + b + "! You just delved into python.") # <- I tried this one
                                                                      # I got it wrong because 
                                                                      # I tried      + a + b + 
                                                                      # instead of + a + " " + b + 

# First off, it took me a while to accept "print()" instead of "return()"
# Secondly, I may have gotten this right much sooner,
# but I didn't seem to debug it properly, 
# and assumed a few otherwise correct answers as wrong.
# For example, I returned "deleved" instead of "delved"
# and instead of inspecting WHAT failed the Testcase,
# I simply said "Welp, that didn't work" and tried other means.
