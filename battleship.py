import os
import string
from bs_cursor import Cursor
from enums import Players, Modes
from colorama import Fore, Back, Style

get_move_text = "please select place to fire in indicated order \"row\" \"col\" : "
place_ship_text = "please select place for you ship : "


# INPUT
def convert_input_to_coordinates(user_input):
    row = user_input[0]
    col = user_input[1]

    row = string.ascii_uppercase.index(row)
    col -= 1

    return row, col


def get_move(board):
    board_size = len(board)
    row_headers = list(map(lambda x: x + 1, list(range(board_size))))
    col_headers = string.ascii_uppercase[:board_size]

    user_input = input("Provide coordinates (e.g. A1): ").upper()
    while user_input[0] not in col_headers or user_input[1] not in row_headers:
        user_input = input("Provide coordinates (e.g. A1): ").upper()
    return user_input


def place_ship(board, row, col, ship_size=1):
    if ship_size == 1:
        if board[row][col] == "0":
            board[row][col] = "S"
            print(f"Place {row},{col} has been taken!")
    return board


def is_next(board, x, y, i, ship_len=1):
    z = ship_len-1
    if i == 1:
        return True     
    elif board[x-z][y] == "S":
        return True
    elif board[x+z][y] == "S":
        return True
    elif board[x][y-z] == "S":
        return True
    elif board[x][y+z] == "S":
        return True
    else:
        print("position the ship in a straight line")
        return False


def get_ai_move():
    pass


# OUTPUT
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


def display_two_boards(board1, board2, offset=4):
    board_size = len(board1)
    column_headers = map(lambda x: str(x + 1), list(range(board_size)))
    row_headers = string.ascii_uppercase[:board_size]

    header = ('  ' + ' '.join(column_headers) + " " * offset) * 2
    print(header)

    # Build rows
    index = 0
    while index < board_size:
        row_string = row_headers[index]
        row_string += ' ' + ' '.join(board1[index])

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


def display_logo():
    print(r"$$$$$$$\   $$$$$$\ $$$$$$$$\ $$$$$$$$\ $$\       $$$$$$$$\  $$$$$$\  $$\   $$\ $$$$$$\ $$$$$$$\  ")
    print(r'$$  __$$\ $$  __$$\\__$$  __|\__$$  __|$$ |      $$  _____|$$  __$$\ $$ |  $$ |\_$$  _|$$  __$$\ ')
    print(r'$$ |  $$ |$$ /  $$ |  $$ |      $$ |   $$ |      $$ |      $$ /  \__|$$ |  $$ |  $$ |  $$ |  $$ |')
    print(r'$$$$$$$\ |$$$$$$$$ |  $$ |      $$ |   $$ |      $$$$$\    \$$$$$$\  $$$$$$$$ |  $$ |  $$$$$$$  |')
    print(r'$$  __$$\ $$  __$$ |  $$ |      $$ |   $$ |      $$  __|    \____$$\ $$  __$$ |  $$ |  $$  ____/ ')
    print(r'$$ |  $$ |$$ |  $$ |  $$ |      $$ |   $$ |      $$ |      $$\   $$ |$$ |  $$ |  $$ |  $$ |      ')
    print(r"$$$$$$$  |$$ |  $$ |  $$ |      $$ |   $$$$$$$$\ $$$$$$$$\ \$$$$$$  |$$ |  $$ |$$$$$$\ $$ |      ")
    print(r'\_______/ \__|  \__|  \__|      \__|   \________|\________| \______/ \__|  \__|\______|\__|      ')


def display_menu(mode):
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
          "3 - Exit")


def display_mode_menu():
    os.system("cls || clear")
    print("Game mode: ", "\n")
    print("Modes: \n"
          "1 - HUMAN-HUMAN\n"
          "2 - HUMAN-AI\n"
          "back - go to menu\n")


def display_select_ship_menu(current_player):
    print(current_player)


# LOGIC
def init_board(size=5):
    board = []
    row = []
    while len(row) < size:
        row.append("0")
    while len(board) < size:
        copy_row = row.copy()
        board.append(copy_row) 
    return board


# wrazie problemów https://pypi.org/project/colorama/  i zmiana wywoływania koloru.
def mark_move(row, col, board, enemy_board):
    if enemy_board[row][col] == "0":
        board[row][col] = Fore.BLACK + "V" + Style.RESET_ALL
        enemy_board[row][col] = Fore.BLACK + "V" + Style.RESET_ALL
    elif enemy_board[row][col] == "S":
        board[row][col] = Fore.RED + "X" + Style.RESET_ALL
        enemy_board[row][col] = Fore.BLACK + "X" + Style.RESET_ALL
    return board


def main_menu(mode):
    display_menu(mode)
    user_input = input("Your pick: ")
    choices = ['1', '2', '3']
    while user_input not in choices:
        user_input = input('Incorrect value. Your pick: ')

    if user_input == '1':
        game(mode)
    elif user_input == '2':
        display_mode_menu()
        mode_menu()
    elif user_input == '3':
        print()
        print("Good bye! See you next time.")
        input("Press enter to continue...")


def mode_menu(mode):
    display_mode_menu()
    user_input = input("Your pick: ").lower()
    choices = ['1', '2', 'back']
    while user_input not in choices:
        user_input = input('Incorrect value. Your pick: ').lower()
    if user_input == '1':
        mode = Modes.HUMAN_HUMAN
    elif user_input == '2':
        mode = Modes.HUMAN_AI
    elif user_input == 'back':
        display_menu()
        # main_menu()


def game(mode):
    board = init_board()
    current_player = Players.Player1


if __name__ == "__main__":
    current_mode = Modes.HUMAN_HUMAN
    main_menu(current_mode)
