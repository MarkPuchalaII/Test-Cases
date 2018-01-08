# I took this from someone else's code
# I found it in the discussion section for this problem

def capitalize(string):
  for x in string[:].split():
    string = string.replace(x, x.capitalize()) 
  return string
    
if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)

################################################################################

    # Hackerrank's approach

    print(' '.join(word.capitalize() for word in input().split(' ')))
    # Of course their version works better.
    # Of course I'm having trouble understanding it.

    # Today was a bad day for my mental health...
    # I'm not sure I should even be coding right now...
    # LET'S GO PLAY SOME AGE OF EMPIRES!
