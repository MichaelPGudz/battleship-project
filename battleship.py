import os
import string
from bs_cursor import Cursor
from enums import Players, Modes
from colorama import Fore, Back, Style

get_move_text = "please select place to fire in indicated order \"row\" \"col\" : "
place_ship_text = "please select place for you ship : "


# INPUT
def get_coordinates(text, size=5):
    x = True
    while x:
        move_input = input(text).upper()
        list_of_letter = list(map(chr, list(range(65, (size + 65)))))
        list_of_number = list(map(str, list(range(1, (size + 1)))))
        if move_input[0] not in list_of_letter:
            print("provide correct coordinates")   
        elif move_input[1] not in list_of_number:
            print("provide correct coordinates")     
        else:
            row = translate_row(move_input[0], list_of_letter, list_of_number)
            col = int(move_input[1])-1
            x = False
    return row, col


def translate_row(row, list_of_letter, list_of_number):
    list_len = len(list_of_number)
    list_of_number.insert(0, "0")
    list_of_number.remove(str(list_len))
    row_translator = {}
    for key in list_of_letter: 
        for value in list_of_number: 
            row_translator[key] = value 
            list_of_number.remove(value) 
            break

    coordinate_x = row_translator[row]
    return int(coordinate_x)


def place_ship(board, ship_len=1):
    i = 0
    while ship_len > i:
        x = True
        i += 1
        while x:
            x, y = get_coordinates(place_ship_text)
            is_next_bool = is_next(board, x, y, i, ship_len)
            
            if is_next_bool:
                if board[x][y] == "0":
                    board[x][y] = "S"
                    print(f"place {x},{y} has been taken")
                    x = False
                else:
                    print("provide empty coordinates")
            # else:
            #     # x= False
            #     # i-=1
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
    column_headers = []
    row_headers = []
    index = 0
    board_size = len(board)
    while index < board_size:
        column_headers.append(string.ascii_uppercase[index])
        row_headers.append(str(index + 1))
        index += 1

    print('  ' + ' '.join(column_headers))
    index = 0
    for row in board:
        row_string = row_headers[index]
        for col in row:
            row_string += ' ' + str(col)
        index += 1
        print(row_string)


def display_two_boards(board1, board2, offset=4):
    column_headers = []
    row_headers = []
    index = 0
    board_size = len(board1)
    while index < board_size:
        column_headers.append(string.ascii_uppercase[index])
        row_headers.append(str(index + 1))
        index += 1
    header = ('  ' + ' '.join(column_headers) + " " * offset) * 2
    print(header)
    # Build rows
    index = 0
    while index < len(board1):
        row_string = row_headers[index]
        for col in board1[index]:
            row_string += ' ' + str(col)
        row_string += ' ' * offset + row_headers[index]
        for col in board2[index]:
            row_string += ' ' + str(col)
        index += 1
        # Print row
        print(row_string)


def display_board_with_position(board, pos_x=0, pos_y=1):
    """WARNING! Work only in console. In PyCharm i had error."""
    cursor = Cursor()
    column_headers = []
    row_headers = []
    index = 0
    board_size = len(board)
    while index < board_size:
        column_headers.append(string.ascii_uppercase[index])
        row_headers.append(str(index + 1))
        index += 1

    cursor.print_in_position(pos_x, pos_y, '  ' + ' '.join(column_headers))
    index = 0
    for row in board:
        row_string = row_headers[index]
        for col in row:
            row_string += ' ' + str(col)
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


def display_menu():
    os.system("cls || clear")
    print()
    print(display_logo(), "\n")
    print("Game mode: ", "\n")
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


# bedzie problem z kolorem, wyprintowanie jednego zakolorowanego pola koloruje wszystko co jest później
# wrazie problemów https://pypi.org/project/colorama/  i zmiana wywoływania koloru.
# problem powienien byc zażegnany --> Style.RESET_ALL
def mark_move(row, col, board, enemy_board):
    if enemy_board[row][col] == "0":
        board[row][col] = Fore.BLACK + "V" + Style.RESET_ALL
        enemy_board[row][col] = Fore.BLACK + "V" + Style.RESET_ALL
    elif enemy_board[row][col] == "S":
        board[row][col] = Fore.RED + "X" + Style.RESET_ALL
        enemy_board[row][col] = Fore.BLACK + "X" + Style.RESET_ALL
    return board


def main_menu(mode):
    display_menu()
    display_ship()
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
    current_player = Players.Player2


if __name__ == "__main__":
    current_mode = Modes.HUMAN_HUMAN
    main_menu(current_mode)
