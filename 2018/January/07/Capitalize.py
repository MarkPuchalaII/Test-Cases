# Revisiting this one, I found it quite easy.
# My version ended up the same as Hackerrank's approach.
# And I understand every part.
# I think I understand these post for-loops a bit more, too.

def capitalize(s):
  return ' '.join(w.capitalize() for w in s.split(' '))
  
if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)

################################################################################

    # Hackerrank's approach

    print(' '.join(word.capitalize() for word in input().split(' ')))
    #Check out how similar our versions were! <3
