"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcounter = 0
    Ocounter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                Xcounter += 1
            elif board[i][j] == O:
                Ocounter += 1
    
    if Xcounter > Ocounter:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))

    return possibleActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_move = player(board)
    new_board = deepcopy(board)

    if board[action[0]][action[1]] != EMPTY:
        raise Exception("This place is already taken.")
    else:
        new_board[action[0]][action[1]] = player_move
    
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontal
    for i in board:
        if i.count(X) == 3:
            return X
        elif i.count(O) == 3:
            return O
    
    #vertical
    for i in range(3):
        column = [board[x][i] for x in range(3)]
        if column == [X, X, X]:
            return X
        elif column == [O, O, O]:
            return O
    
    #diagonal
    temp_check1 = board[0][0]
    temp_check2 = board[0][2]

    if temp_check1 == board[1][1] and temp_check1 == board[2][2]:
        return temp_check1
    elif temp_check2 == board[1][1] and temp_check2 == board[2][0]:
        return temp_check2

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for i in range(3):
        row = [board[i][x] for x in range(3)]
        if EMPTY in row:
            return False
    
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    playerThatWon = winner(board)

    if playerThatWon == X:
        return 1
    elif playerThatWon == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -5
            for action in actions(board):
                minval = min_value(result(board, action))[0]
                if minval > v:
                    v = minval
                    optimal_move = action
            return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = 5
            for action in actions(board):
                maxval = max_value(result(board, action))[0]
                if maxval < v:
                    v = maxval
                    optimal_move = action
            return v, optimal_move

    curr_player = player(board)

    if terminal(board):
        return None

    if curr_player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]