def count_substring(string, sub_string):
    c = 0
    for i in range(0,(len(string)-len(sub_string)+1)):
      if(string[i:i+len(sub_string)] == sub_string) : c += 1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

################################################################################

# Hackerrank's approaches


# Approach 1
# Slice an x amount of string in each iteration of the loop. 
A = raw_input().strip()
x = raw_input().strip()

count = 0
for i in range(len(A) - len(x) + 1):
    if A[i:i+len(x)] == x:
        count += 1
print count



# Approach 2
# This can be solved by using a regex.
import re
a = raw_input()
b = raw_input()
match = re.findall('(?='+b+')',a)
print len(match)
