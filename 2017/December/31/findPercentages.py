# This challenge had me create dictionaries based on:
# 'person' : mathScore, physicsScore, chemistryScore
#
# The core task was to find the average between these three scores
# for whichever person is named in the final output

if __name__ == '__main__':
    a = {}                            # I did a pretty good job
    for x in range(int(input())) :    # first input determines Dictionary's size
        n, *c = input().split()       # split the input based on 'name , score, score, score'
        a[n] = list(map(float, c))    # Then assigning the key as 'name : score, score, score'

    qr = input()                                     # Finally, we ask for input
    print("%.2f" % ((a[qr][0]+a[qr][1]+a[qr][2])/3)) # and we find the average of that key's values.

################################################################################

if __name__ == '__main__':
d={}                            # Hackerrank, as always, was even more elegant.
for i in range(int(input())):   # They detemined the Dictionary's size the same way I did.
	line=input().split()        # Then split the input as a single array.
	d[line[0]]=sum(map(float,line[1:]))/3  # and stored the array as simply 'name' : average
                                # Since they stored the average from the start
print ('%.2f' % d[input()])     # They were able call the final input without any complexities.

  ## Notes ##
  # My greatest lesson learned, here, is relevance.
  # My thought was as follows:
  #  - collect a person's name and their score
  #  - Store 'name' : score , score, score
  #  - Call on a person
  #  - Find and print the average of that person's scores
  #
  # The Problem Tester's mindframe was as follows:
  #  - collect a person's name and their scores
  #  - store 'name' : averageOfThoseScores
  #  - Call on anyone
  #
  # I can see, here, how the Problem Tester noticed ahead of time
  # that the individual scores were not important - only their average.
  # because of this, there was no point in storing them individually.
  # So the Problem Tester saved time & effort by calculating the average
  # just before storing it.
  # Again, their thought was :
  #    1. get scores,
  #    2. average them, 
  #    3. store it,
  #    4. call it any time.
  # That's much cleaner than :
  #    1. get scores,
  #    2. store them,
  #    3. get input,
  #    4. average scores,
  #    5. report it.
