import numpy as np
import datetime

# Set starting conditions
board = np.zeros((6, 7))
game_on = True
player = 1
pieces_in_board = 0
FULL = 42 # 6 rows x 7 cols