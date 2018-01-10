# Probably put way more research into this than I needed to
# Mainly because I was multitasking between this, Game Grumps, and Runescape
# Still, my solution ended up much more elegant & simple thank Hackerrank's
# And I understand a variety of things better
# namely the max() function, numpy, scipy, and that odd [, var] parameter

# Lesson learned is SERIOUSLY MULTI-TASK LESS. IT'S YOUR NEW YEARS RESOLUTION.

def average(array):
  return(sum(set(array)) / len(set(array)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

################################################################################

    # Hackerrank's approaches
    
from __future__ import division
n = int(raw_input())
heights = [int(x) for x in raw_input().split()] 

#Step 1 - Make Set -  Store the set of inputs in the variable distinctHeights.
distinctHeights = set(heights)

#Step 2 - Summation of Set - Store the sum of distinctHeights in the variable sumOfDistinctHeights.
sumOfDistinctHeights = sum(distinctHeights)

#Step 3 - Length of Set - Store the total number of distinctHeights in the variable totalDistinctHeights.
totalDistinctHeights = len(distinctHeights)

#Step 4 - Take Average - Take the average by dividing the sumOfDistinctHeights with totalDistinctHeights.
average = sumOfDistinctHeights/totalDistinctHeights

#Step 5 - Print Output - Print the output.
print average
