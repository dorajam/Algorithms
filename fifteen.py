# -*- coding: utf-8 -*-
# Dora Jambor, dorajambor@gmail.com
# January, 2016
# Implementation of the game fifteen in Python

from Tkinter import *

# ---------- parameters ----------
# Dimensions
min_dim = 3
max_dim = 9

# Location of blank space
blankx = 0
blanky = 0

# ---------- functions ----------
def greet():
    print 'This is the Game of Fifteen!'

def dim():
    result = int(raw_input('Insert the dimension of the board: '))
    while True:
        if result >=min_dim and result <= max_dim:
            break
        result = int(raw_input('Try again: '))
    return result    
            
            
# Play the game
'''
A function called by Tkinter that allows the user to interact with the game board 
and play the game by moving the tiles.
'''   
def play(i,j):
    global blankx, blanky, game_running
    
    if game_running:
        # update vars if tile can be moved
        if (blankx, blanky) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            board[blanky][blankx].set(board[j][i].get())
            board[j][i].set(' ')
            
            blanky = j
            blankx = i
            
            if won():
                # lable is now visible
                bn.lift()
                game_running = False
    
                                                                        
def won():
    number = 0

    for j, row in enumerate(board):
        for i, string_var in enumerate(row,1):
            number += 1
            if number == d * d and string_var.get() == ' ':
                return True
            elif string_var.get() != str(number):
                return False
    return True


# Initialize the board 
'''
This sets up/resets all data and variables - and fills and updates board with numbers.
'''
def setup():
    global blankx, blanky, game_running
    # set blank coordinates
    blankx = d - 1
    blanky = d - 1
    
    # this is where bn is marked as not defined - "global name 'bn' is not defined"
    bn.lower()
    
    # fill/update board with numbers
    numbers = d * d
    
    for row in board:
        for tile in row:
            numbers -= 1
            if numbers == 0:
                tile.set('')
            else:
                tile.set(str(numbers))

    # continue game
    game_running = True


    
# ---------- main ----------
greet()
d = dim()

board = []


# --- 1.) Initialization of the UI and event handlers ---
# create window
root = Tk()
root.config(bg = 'white', borderwidth=4)
root.wm_title("Game of Fifteen")

# button for winning
bn = Button(root, text="You won!\n <click to start>", command=setup)
bn.grid(row=0, column=0, ipadx=3, ipady=10)

# frame for the board game
frame = Frame(root)
frame.config(bg='black',borderwidth=2)
frame.grid(row=0, column=0)


# fill board with StringVars
for i in range(d):
    row = []
    for j in range(d):
        var_text = StringVar()
        row.append(var_text)
    board.append(row)

# update board vars with initial numbers
setup()

 #visualize board on frame - start playing            
for j, row in enumerate(board):
    for i, string_var in enumerate(row):
        b = Label(frame, textvariable=string_var, bg='pink', width=2, height=1, font=("Times", 30, 'bold'), relief=RAISED)  
        b.grid(row=j, column=i, sticky="nsew", ipadx=8, padx=4, pady=4)
        b.bind('<Button-1>',lambda e, i=i,j=j:play(i,j))

# --- 2.) Initialization of the event loop - start engine---
root.mainloop()  