import numpy as np 
import random
import os
from IPython.display import clear_output
import time

# game logic
"""
1. 4 * 4 grid(matrix) for game play  
initially there would be 2 random cells with a number 2 in it, therest are empty
2. generate a new random 2 for an empty cell in each round
3. Users can press w, s, a, d to move up, down, left, or right. When users press any key,
the elements of the cell move in that direction
4. in the move, if any two numbers
are at the same row when you move horizontally, or in the same column
when you move vertically they get added up in that direction and fill itself
with that number, the rest cells go empty again.
5.  If no numbers are the same
and next to each other with one move, all numbers will move to the same
direction to fill all the space at that row/column. 
6. If you reach 2048, you win the game, end the game or restart the game
7. If you cannot make further moves, end the game or restart the game
8. you need to use exception handling to handle all invalid inputs
"""
def add_new_number(board): 
    empty_cell = [(r,c) for r in range (4) for c in range(4) if board[r,c] ==0]
    if empty_cell:
        row, col = random.choice(empty_cell)
        board[row, col] = 2
    #else

def initialize_game(): 
    board = np.zeros((4,4), dtype = int)
    add_new_number(board)
    add_new_number(board)
    return board

def move_left(board):
    new_board = np.zeros_like(board)
    for i in range(4):
        # remove 0s in each row
        row = board[i][board[i] != 0]
        new_row = []
        skip = False
        for j in range(len(row)):
            if skip:
                skip = False
                continue
            if j < len(row) - 1 and row[j] == row[j + 1]: 
                new_row.append(row[j] * 2) 
                skip = True
            else:
                new_row.append(row[j])
        new_board[i, :len(new_row)] = new_row
    return new_board

def move_right(board): 
    return np.fliplr(move_left(np.fliplr(board)))

def move_down(board):
    return np.rot90(move_left(np.rot90(board, -1)), 1)

def move_up(board):
    return np.rot90(move_left(np.rot90(board, 1)), -1)

def is_game_over(board): 
    if 2048 in board: 
        print("you win!")
        return True
    if not any(0 in rows for rows in board): 
        for move in [move_left, move_right, move_up, move_down]:
            if not np.array_equal(board, move(board)):
                return False
        print("game over since there is no more move you can make.")
        return True
    return False

def print_board(board): 
    clear_output(wait=True)
    time.sleep(0.05)
    print("\n".join(["\t".join(map(str, row)) for row in board]))