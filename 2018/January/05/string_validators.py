if __name__ == '__main__':
    s = input()
    c2 = [False for each in range(0,5)]
    for each in s :
      if not c2[0] and each.isalnum() : c2[0] = True
      if not c2[1] and each.isalpha() : c2[1] = True
      if not c2[2] and each.isdigit() : c2[2] = True
      if not c2[3] and each.islower() : c2[3] = True
      if not c2[4] and each.isupper() : c2[4] = True
    for each in c2 : 
      print(each)
################################################################################

# Hackerrank's approach
S = raw_input()
print any([char.isalnum() for char in S])  # So not only do these validation
print any([char.isalpha() for char in S])  # methods work with char as well as string
print any([char.isdigit() for char in S])  # 
print any([char.islower() for char in S])  # But Python has an ANY function!?
print any([char.isupper() for char in S])  # Holy hell I love this language!

# In retrospect, I realize "char" was the variable name. 
# I don't know if validation methods actually work with chars or not.
# Maybe Python doesn't even have chars.
# I'd rather let it come up in future challenges than test it now.
