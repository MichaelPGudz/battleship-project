import Output
from enums import Players
board1 = [['O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O']]
players = [Players.Player1, Players.Player2]
Output.display_two_boards(board1, board1, players)

