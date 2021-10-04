from tictactoe import result

X = "X"
O = "O"
EMPTY = None

board = [[X, X, EMPTY],
        [O, EMPTY, O],
        [EMPTY, EMPTY, X]]

action = ((1, 1))

print(result(board, action))
