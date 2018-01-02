def mutate_string(string, position, character): # I used the slicing strategy
    return string[:position] + character + string[position+1:]
  
if __name__ == '__main__':
  s = input()
  i, c = input().split()
  s_new = mutate_string(s, int(i), c)
  print(s_new)

################################################################################

# Beginning to think the problem testers DELIBERATELY make these challenges
# So that I won't be able to get it as good as the problem testers do.

  s = raw_input()                    # I can see they first take the string
i,k = raw_input().split()            # Then they take the position & characters
print s[:int(i)]+k+s[int(i)+1:]      # And place that character based on the position

################################################################################

def mutate_string(string, position, character): # Here's my attempt at a list!
    l = list(string)           # I am proud to declare I did this by memory
    l[position] = character    # I didn't have to consult or reference anything!
    return ''.join(l)   # <- Except this part. I tried "return string(l)". 
                        # I didn't yet know to try something like ''.join(l)
if __name__ == '__main__':
  s = input()
  i, c = input().split()
  s_new = mutate_string(s, int(i), c)
  print(s_new)
