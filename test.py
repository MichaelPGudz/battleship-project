import Output
import battleship
from colorama import *
from enums import Players

board1 = [['0', '0', '0', '0', '0'],
          ['0', 'X', '0', '0', '0'],
          ['0', '0', 'X', 'X', '0'],
          ['0', '0', '0', '0', '0'],
          ['0', '0', '0', '0', '0']]
players = [Players.Player1, Players.Player2]
battleship.make_edges(board1)
Output.color_specific_sign(board1, 'X', Fore.RED)
Output.display_two_boards(board1, board1, players)
Output.display_board(board1)
