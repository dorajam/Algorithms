# Dora Jambor, dorajambor@gmail.com
# January, 2016
# Implementation of the game fifteen in Python

import time
import Tkinter as tk

# Dimensions
min_dim = 3
max_dim = 9
d = 0

board = []
counter = 0


# Location of blank space
blankx = 0
blanky = 0

# Introduce the game
def greet():
    #clear()
    print 'GAME OF FIFTEEN'
    time.sleep(0.5)

def dim():
    global min_dim, max_dim, d
    d = int(raw_input('Insert the dimension of the board: '))
    while True:
        if d >=min_dim and d <= max_dim:
            break
        d = int(raw_input('Try again: '))
    return d     
    
# Initialize the board
def init():
    numbers = d * d - 1
    global board, blankx, blanky
    blankx = d - 1
    blanky = d - 1
    board = [[d*d-1-i-d*j for i in range(d)] for j in range(d)]
    board[blankx][blanky] = d * d

        
def draw(d):
    global board
    for i in range(d):
        for j in range(d):
            if board[i][j] == d * d:
                print '_'
            else:
                print board[i][j]
                
def move():
    tile = int(raw_input('Which tile would you like to move: '))
    global board, blankx, blanky
    for i in range(d):
        for j in range(d):
            if(board[i][j] == tile):
                if(i - 1 == blanky or i + 1 == blanky or j - 1 == blankx or j + 1 == blankx):
                    board[i][j] = d * d
                    board[blanky][blankx] = tile
                    blanky = i
                    blankx = j
                    return True
    return False
                
def won():
    for i in range(d-1):
        for j in range(d-1):
            if board[i][j] != board[i+1][j] - 1 or board[i][j] != board[i][j+1]-1:
                return False
    return True

def on_click(i,j,event):
    global counter
    color = "grey" if counter%2 else "red"
    event.widget.config(bg=color)
    board[i][j] = color
    counter += 1

def key(event):
    print "pressed", repr(event.char)

def callback(event):
    window.focus_set()
    print "clicked at", event.x, event.y  

def visualize():
    window = tk.Canvas(width=100, height=100, borderwidth=12, highlightthickness=20,background='bisque')
    for i,row in enumerate(board):
        for j,column in enumerate(row):
            L = tk.Label(root,text='   %s   '%board[i][j],bg='pink')
            L.grid(row=i,column=j)
            if board[i][j] == d*d:
                L = tk.Label(root,text='        ')
            L.grid(row=i,column=j,sticky="nsew", padx=1, pady=1)
            # L.bind('<Button-1>',lambda e,i=i,j=j: on_click(i,j,e))
            #L.bind("<Key>", key)
           # L.bind("<Button-1>", callback)

root = tk.Tk()
root.title = 'GAME FIFTEEN'

def main():
    greet()
    global d
    d = dim()
    init()
    #draw(d)
    # visual
    visualize()
    root.mainloop()

    while won() == False:
        if not (move()):
            print 'Illegal move!'
    print "You won the game!"
    
     
if __name__ == "__main__":
    main()
    

