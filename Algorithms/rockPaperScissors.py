# Dora Jambor
# rockPaperScissors.py
# 5.12.2014

'''
Implements the rock paper scissors game.
'''

player1 = raw_input('Player1? ')
player2 = raw_input('Player2? ')

if player1 != 'scissors' and player1 != 'rock' and player1 != 'paper' and player2 != 'scissors' and player2 != 'rock' and player2 != 'paper':
        print 'This is not valid object selection.'
        
if player1 == 'rock' and player2 == 'scissors':
        print 'Player 1 wins'

if player1 == 'rock' and player2 == 'paper':
        print 'Player 2 wins'

if (player1 == 'rock' and player2 == 'rock'):
        print 'Players tie'

if (player1 == 'scissors' and player2 == 'paper'):
        print 'Player 1 wins'

if (player1 == 'scissors' and player2 == 'rock'):
        print 'Player 2 wins'

if (player1 == 'scissors' and player2 == 'scissors'):
        print 'Players tie'

if (player1 == 'paper' and player2 == 'rock'):
        print 'Player 1 wins'

if (player1 == 'paper' and player2 == 'scissors'):
        print 'Player 2 wins'

if (player1 == 'paper' and player2 == 'paper'):
        print 'Players tie'


