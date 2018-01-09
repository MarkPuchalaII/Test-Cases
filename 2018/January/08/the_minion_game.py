# Used someone else's code, again.
# Today was a terrible day... My car is a total loss.
# I don't want to file bankruptcy...

def minion_game(s):
  vowels = 'AEIOU'

  kevsc, stusc = 0, 0
  for i in range(len(s)):
      if s[i] in vowels: kevsc += (len(s)-i)
      else: stusc += (len(s)-i)

  if kevsc > stusc: print("Kevin", kevsc)
  elif kevsc < stusc: print("Stuart", stusc)
  else: print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

################################################################################

    # Hackerrank's approach
S = raw_input().strip()      # I'm too exhausted from today.
S_length = len(S)            # I will review this later...
player1, player2 = 0,0

for i in xrange(S_length):
    if S[i] in "AEIOU": player1 += S_length - i
    else: player2 += S_length - i        
        
if player1 > player2: print "Kevin", player1
elif player1 < player2: print "Stuart", player2
else: print "Draw"
