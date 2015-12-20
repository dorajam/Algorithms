# Dora Jambor, dorajambor@gmail.com
# nims.py
# 5.12.2014

'''
Implements the nim game, where in two players take turns 
removing objects from a distinct heap. At each turn you need 
to remove at least one object, and may remove any number of objects provided they all come from the same heap.
The goal is to be the player to remove the last object.
'''

def nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''
    current_player = 0

    while pile > 0:
        is_valid = False
        
        # as long as it's invalid
        while is_valid == False:
            # get input from the current player
            choice = input("Player " + str(current_player+1) + "," + " Please provide with number: ")

            # Check if invalid input
            if not isinstance(choice, int):
                print("Your input must be an integer!")
                continue
            if choice > max_stones or choice < 1:
                print("Your input must be in the correct range!")
                continue
            if choice > pile:
                print("That's more than the piles left")
                continue

            # if reached, then input is valid, so exit inner loop
            is_valid = True
            pile = pile - choice

        # other player's turn
        current_player = (current_player + 1) % 2

    # no more piles left
    print("Game over")

    # adjust players number from 0,1 to 1,2 and print statement
    print("Player " + str((current_player - 1) % 2 + 1) + " wins!!")


# test
nims(20,5)
