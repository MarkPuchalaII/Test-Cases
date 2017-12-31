if __name__ == '__main__':                   # This was my original attempt
  x = []                                     # Wow, I don't know this language
  for _ in range(int(input())):              # Spaghetti code, anyone?
    name = input()
    score = float(input())      # So I started with Hackerrank's input
    x.append([score, name])     # Plugged it all into my own list, x.
  x.sort()                      # Sorted that list,
  a = b = min(x)[0]             # Then set a & b to its first nested list.
  i = 0                         # i is my iterator that I "cleverly" made two uses for.
  while b == a :                # (more on that later)
      i += 1                    # I'm iterating through the list
      if b < x[i][0] :          # So that b is SECOND to smallest
          b = x[i][0]           # while a stays smallest.

  z = []                                # Now I create a second list
  while i != len(x) and x[i][0] == b :  # That holds ONLY names whos' respective numbers
      z.append(x[i])                    # are equal to b, our "second smallest"
      i +=1    # Note how I'm using the PREVIOUS i. I START where the previous loop left off

  for e in z :     # Once my complicated mess is done
    print(e[1])    # I finally print everything in Z.
                   # I evidently assume it to be sorted, since the previous list was sorted.

################################################################################
# This was HackerRank's version
if __name__ == '__main__':
  a = [[input(), float(input())] for x in range(int(input))] # I find this unreadable as fuck
  s = sorted(set([x[1] for x in a]))                         # Still, it's more compact than mine.
  for n in (sorted(x[0] for x in a if x[1] == s[1])) :       # 4 lines to my 21.
    print(n)

    # NOTES #
    # - First off, I'm takin this "sorted(set([i]))" practice.
    #   sorted sets are a pretty neat way to organize thins quickly
    #
    # - Secondly, I need to focus more on consolidating my code.
    #   It's not just "get to the next step."
    #   What I see from this example is as follows :
    #     Create a set to hold your data
    #     Create a second set to test it against
    #     Work from there
    #  While I could have said this much more compassionately, I get the message.
    #  I have a new practice to clean up my future code.
    #  Can't wait to test it out! Working with nested lists was memorable.
