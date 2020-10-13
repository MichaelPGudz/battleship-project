import os
import string
from bs_cursor import Cursor


def display_menu(mode, board_size=5):
    os.system("cls || clear")
    print()
    display_logo()
    print()
    display_ship()
    print()
    mode = str(mode).split('.')[1]
    print("Game mode: ", mode, "\n")
    print("MENU:\n"
          "1 - Start Game\n"
          "2 - Game Modes\n"
          f"3 - Set board size (current: {board_size})\n"
          "4 - Exit")


def display_mode_menu(mode):
    os.system("cls || clear")
    print(f"Game mode: {mode}", "\n")
    print("Modes: \n"
          "1 - HUMAN-HUMAN\n"
          "2 - HUMAN-AI\n"
          "back - go to menu\n")


def display_logo():
    print(r"$$$$$$$\   $$$$$$\ $$$$$$$$\ $$$$$$$$\ $$\       $$$$$$$$\  $$$$$$\  $$\   $$\ $$$$$$\ $$$$$$$\  ")
    print(r'$$  __$$\ $$  __$$\\__$$  __|\__$$  __|$$ |      $$  _____|$$  __$$\ $$ |  $$ |\_$$  _|$$  __$$\ ')
    print(r'$$ |  $$ |$$ /  $$ |  $$ |      $$ |   $$ |      $$ |      $$ /  \__|$$ |  $$ |  $$ |  $$ |  $$ |')
    print(r'$$$$$$$\ |$$$$$$$$ |  $$ |      $$ |   $$ |      $$$$$\    \$$$$$$\  $$$$$$$$ |  $$ |  $$$$$$$  |')
    print(r'$$  __$$\ $$  __$$ |  $$ |      $$ |   $$ |      $$  __|    \____$$\ $$  __$$ |  $$ |  $$  ____/ ')
    print(r'$$ |  $$ |$$ |  $$ |  $$ |      $$ |   $$ |      $$ |      $$\   $$ |$$ |  $$ |  $$ |  $$ |      ')
    print(r"$$$$$$$  |$$ |  $$ |  $$ |      $$ |   $$$$$$$$\ $$$$$$$$\ \$$$$$$  |$$ |  $$ |$$$$$$\ $$ |      ")
    print(r'\_______/ \__|  \__|  \__|      \__|   \________|\________| \______/ \__|  \__|\______|\__|      ')


def display_ship():
    print(r'              |    |    |               ')
    print(r'             )_)  )_)  )_)              ')
    print(r'            )___))___))___)\            ')
    print(r'           )____)____)_____)\\          ')
    print(r'         _____|____|____|____\\\__      ')
    print(r'---------\                   /--------- ')
    print(r'  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^           ')
    print(r'    ^^^^      ^^^^     ^^^    ^^        ')
    print(r'         ^^^^      ^^^                  ')


def display_board(board):
    board_size = len(board)
    column_headers = map(lambda x: str(x + 1), list(range(board_size)))
    row_headers = string.ascii_uppercase[:board_size]

    header = '  ' + ' '.join(column_headers)
    print(header)
    index = 0
    for row in board:
        row_string = row_headers[index]
        row_string += ' ' + ' '.join(row)
        index += 1
        print(row_string)


def display_two_boards(board1, board2, players, offset=4):
    board_size = len(board1)
    column_headers = map(lambda x: str(x + 1), list(range(board_size)))
    row_headers = string.ascii_uppercase[:board_size]

    displayed_row_length = 2 * board_size + 1
    print(str(players[0]).split('.')[1].rjust(displayed_row_length) +
          str(players[1]).split('.')[1].rjust(displayed_row_length + offset))
    header = ('  ' + ' '.join(column_headers) + " " * offset) * 2
    print(header)

    # Build rows
    index = 0
    while index < board_size:
        # First player rows
        row_string = row_headers[index]
        row_string += ' ' + ' '.join(board1[index])
        # Second player rows
        row_string += ' ' * offset + row_headers[index]
        row_string += ' ' + ' '.join(board2[index])

        index += 1
        print(row_string)


def display_board_with_position(board, pos_x=0, pos_y=1):
    """WARNING! Work only in console. In PyCharm i had error."""
    cursor = Cursor()
    board_size = len(board)
    column_headers = map(lambda x: str(x + 1), list(range(board_size)))
    row_headers = string.ascii_uppercase[:board_size]

    header = '  ' + ' '.join(column_headers)
    cursor.print_in_position(pos_x, pos_y, header)
    index = 0
    for row in board:
        row_string = row_headers[index]
        row_string += ' ' + ' '.join(row)
        index += 1
        cursor.print_in_position(pos_x, pos_y + index, row_string)


def display_set_ships_playground(board, current_player):
    os.system("cls || clear")
    display_ship()
    print("\nSet your ships!\n")
    display_board(board)
    print(f"\nCurrent player: {str(current_player).split('.')[1]}")


def display_playground(board1, board2, players, current_player):
    os.system("cls || clear")
    display_ship()
    print()
    display_two_boards(board1, board2, players)
    print(f"\n{str(current_player).split('.')[1]} turn")
