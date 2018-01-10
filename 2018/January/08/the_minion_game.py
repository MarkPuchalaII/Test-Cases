# Figured this one out quite easily after review.
# My main issue was that I didn't figure out the trick to this game.
# So I overcomplicated things, trying to solve uneccessary puzzles.

def minion_game(w):
    v = 'AEIOU'
    k, s = 0, 0
    
    for i in range(len(w)):
        if w[i] in v : k += len(w)-i # Checkout how elegant my version was this time.
        else         : s += len(w)-i # I'm proud of this one, now. ;)    
    
    if   k > s : print('Kevin ' , k)
    elif s > k : print('Stuart ', s)
    else       : print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)

################################################################################

    # Hackerrank's approach
S = raw_input().strip()   
S_length = len(S)       
player1, player2 = 0,0

for i in xrange(S_length):
    if S[i] in "AEIOU": player1 += S_length - i
    else: player2 += S_length - i        
        
if player1 > player2: print "Kevin", player1
elif player1 < player2: print "Stuart", player2
else: print "Draw"
