from tictactoe import winner
from tictactoe import terminal
from tictactoe import utility
X = "X"
O = "O"
EMPTY = None

board = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]

print(winner(board))
print(terminal(board))
print(utility(board))