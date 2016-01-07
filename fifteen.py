# -*- coding: utf-8 -*-
# Dora Jambor, dorajambor@gmail.com
# January, 2016
# Game of Fifteen, fifteen.py
'''
This is my implementation of game of fifteen using the Tkinter module for GUI, 
while allowing you to play on an actual game board.
Numbers in the tiles will be set up in a descending order. 
Your task is to move tiles one by one to reorder them to ascent, 
with the blank space placed in the bottom right corner.
Press return to reset the initial numbers.
'''

from time import sleep
from Tkinter import *

# -------------------- parameters --------------------
# dimensions
min_dim = 3
max_dim = 9

# global for key input
keybuf=[]

# location of blank space
blankx = 0
blanky = 0

# -------------------- functions --------------------
# intro before setting up the game board
def greet():
    print 'This is the Game of Fifteen!'

def dim():
    result = int(raw_input('Insert the dimension of the board: '))
    while True:
        if result >=min_dim and result <= max_dim:
            break
        result = int(raw_input('Try again: '))
    return result   
     

# setting up functions (events) in Tkinter
'''
This sets up/resets all data and variables - and updates board with numbers.
'''
def setup(event=None):
    global blankx, blanky, game_running
    
    # set blank coordinates
    blankx = d - 1
    blanky = d - 1
    
    # hide the 'winner' label
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
                                    
            
# play the game
'''
A function (event) called by Tkinter that allows the user to interact with the game board 
and play the game by moving the tiles.
'''   
def play(i,j):
    global blankx, blanky, game_running
    
    welcome.lower()
    if game_running:
        # update vars if tile can be moved
        if (blankx, blanky) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            board[blanky][blankx].set(board[j][i].get())
            board[j][i].set(' ')
            
            # reset blank coordinates
            blanky = j
            blankx = i
            
            if won():
                # lable is now visible
                bn.lift()
                game_running = False
                
    
# check if game completed
'''
The function checks whether the numbers on the tiles are ascending, 
and whether the blank space is in the bottom right corner.
'''                                                                           
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

    
# key events
'''
These are the <key> events that enable your keyboard to move tiles with.
''' 
# handling double digit numbers
def test_after():
    global keybuf
    
    # check if empty
    if keybuf:
        # get all keys in buffer as one text
        text = ''.join(keybuf)
        print text
        for j, row in enumerate(board):
            for i, char in enumerate(row):
                if char.get() == text:
                    # swop tiles
                    play(i,j)
                    
                    # clear list
                    keybuf = []
                    return     
                          
def key(event):
    global keybuf
    keybuf.append(event.char)
    root.after(500, test_after)
    
                                    
def right_Key(event):
    i = blankx + 1
    j = blanky
    if 0 <= i < d and 0 <= j < d:
        play(i,j)
    
def left_Key(event):
    i = blankx - 1
    j = blanky
    if 0 <= i < d and 0 <= j < d:
        play(i,j)  
            
def up_Key(event):
    i = blankx
    j = blanky - 1
    if 0 <= i < d and 0 <= j < d:
        play(i,j)
        
def down_Key(event):
    i = blankx
    j = blanky + 1
    if 0 <= i < d and 0 <= j < d:
        play(i,j)


# helper function to solve 3x3 board
def automate(event):
    path = [1,2,5,4,3,1,2,3,4,8,7,6,1,2,3,4,6,1,2,3,4,5,8,7,1,2,3,4,5,6,4,5,6,8,7,4,5,6]
    k=0
    while(k < 38):
        for j, row in enumerate(board):
            for i, char in enumerate(row):
                if char.get() == str(path[k]):
                    play(i,j)
                    k +=1                  
    
    
# -------------------- main --------------------
# intro functions
greet()
d = dim()

# set board as global
board = []


# --- 1.) Initialization of the UI and event handlers ---
# create window
root = Tk()
root.config(bg = 'white', borderwidth=4)
root.wm_title("Game of Fifteen")

# binding key events
root.bind('<Key>', key)
root.bind('<Right>', right_Key)
root.bind('<Left>', left_Key)
root.bind('<Up>', up_Key)
root.bind('<Down>', down_Key)

# automated test only for 3x3 board
root.bind("<space>", automate)

# create welcome label
welcome = Label(root, text="Hi there! \n < click on board to start >",font=("Times", 13, 'bold'), relief=RAISED)
welcome.config(bg='black',fg='pink',borderwidth=2)
welcome.grid(row=0, column=0, ipadx=3, ipady=10)

# create button for winning
root.bind("<Return>", setup)
bn = Label(root, text="Good job!\n < click return to start >",font=("Times", 13, 'bold'), relief=RAISED)
bn.config(bg='black',fg='pink',borderwidth=2)
bn.grid(row=0, column=0, ipadx=3, ipady=10)

# create frame for the board game
frame = Frame(root)
frame.config(bg='black',borderwidth=2)
frame.grid(row=0, column=0)


# -------------------- board --------------------
# Initialize the board list filling each list with StringVar()
for i in range(d):
    row = []
    for j in range(d):
        var_text = StringVar()
        row.append(var_text)
    board.append(row)

# reset board with initial numbers
setup()

#visualize board on frame - start playing            
for j, row in enumerate(board):
    for i, string_var in enumerate(row):
        b = Label(frame, textvariable=string_var, bg='pink', width=2, height=1, font=("Times", 30, 'bold'), relief=RAISED)  
        b.grid(row=j, column=i, sticky="nsew", ipadx=8, padx=4, pady=4)
        b.bind('<Button-1>',lambda e, i=i,j=j:play(i,j))

#welcome label
welcome.lift()
                

# --- 2.) Initialization of the event loop, starting engine ---
root.mainloop()  