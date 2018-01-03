# The point of this exercise was to shift an array to the left.
# You take an array of length n,
# decide to shift it left k times.
# Then you populate the array.
# And then you perform that left shift.

# I didn't actually "left-shift" anything.
# Instead I found where the "starting point" would be after k shifts,
# And I populated a second array from that starting point,
# looping back to the beginning of the array once it's reached the end.

# I'm very proud of my algorithm, as it doesn't make any explicit decisions 
# to loop back to the beginning. Instead it simply counts up "n times"
# from a negative number based on where it left-shifted to.


def array_left_rotation(a, n, k):
    k *= -1         # I set the starting point based on "k positions" in reverse
    a2 = a[:]       # I made a copy of the array (might be better with an empty of len(a))
    for each in a : # Then for every item in a
      a2[k] = each  # I put it in a2
      k += 1        # starting from however many positions k shifted us left.

    for each in a2 :         # After that, I loop through the second array, printing each part.
      print(each, end = " ") # I don't like how there's a space after the final item.
                               # The following code was provided by the example.
n, k = map(int, input().strip().split(' '))     # First get n, and k.
a = list(map(int, input().strip().split(' ')))  # Then populate the array, a.
answer = array_left_rotation(a, n, k);          # create the left-shifted version.
print(*answer, sep=' ')                         # And then print it all back out.
