import os
import string
from bs_cursor import Cursor
from enums import Players, Modes
from colorama import Fore, Style


# INPUT
def convert_input_to_coordinates(user_input):
    row = user_input[0]
    col = user_input[1:]

    row = string.ascii_uppercase.index(row)
    col -= 1

    return row, col


def get_move(board):
    board_size = len(board)
    row_headers = list(map(lambda x: x + 1, list(range(board_size))))
    row_headers = [str(element) for element in row_headers]
    col_headers = string.ascii_uppercase[:board_size]

    user_input = input("Provide coordinates (e.g. A1): ").upper()
    while user_input[0] not in col_headers or user_input[1] not in row_headers:
        user_input = input("Please try again. Provide coordinates (e.g. A1): ").upper()
    return user_input


# def place_ship(board, row, col, ship_size=1):
#     if ship_size == 1:
#         if board[row][col] == "0":
#             board[row][col] = "S"
#             print(f"Place {row},{col} has been taken!")
#     return board
#Bottom Jarek


# INPUT
def get_board_size():
    board_size = input("Please enter number of columns in the board: ")
    while not board_size.isdigit() or int(board_size) < 5 or int(board_size) > 10:
        board_size = input("Wrong value, please try again!")
    return int(board_size)


def get_coordinates(ship_size=None, board_size=5):
    assignment_bool = True
    while assignment_bool:
        move_input = input(f"Please select coordinates in indicated order "
                           f"\"row\" \"col\" (ship size: {ship_size}): ").upper()
        list_of_letter = list(map(chr, list(range(65, (board_size + 65)))))
        list_of_number = list(map(str, list(range(1, (board_size + 1)))))
        if move_input[0] not in list_of_letter or move_input[1] not in list_of_number:
            print("Provide correct coordinates!")
        else:
            row = translate_row(move_input[0], list_of_letter, list_of_number)
            col = int(move_input[1:])-1
            assignment_bool = False
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
    while_loop_counter = 0
    while ship_len > while_loop_counter:
        assignment_bool = True
        while_loop_counter += 1
        while assignment_bool:
            row, col = get_coordinates(ship_len)
            is_next_bool = is_next(board, row, col, while_loop_counter, ship_len)
            if is_next_bool:
                if board[row][col] == "0":
                    board[row][col] = "S"
                    print(f"place {row},{col} has been taken")
                    assignment_bool = False
                else:
                    print("provide empty coordinates")
            # else:
            #     # x= False
            #     # i-=1
    return board


def is_next(board, x, y, loop_counter, ship_len=1):
    len_board = len(board)-1
    len_ship_to_place = loop_counter-1
    if loop_counter == 1:
        return True
    elif x == 0 and y == 0:
        if board[x+len_ship_to_place][y] == "S" and board[x+1][y] == "S":
            return True
        elif board[x][y+len_ship_to_place] == "S" and board[x][y+1] == "S":
            return True
        else:
            print("position the ship in a straight line")
            return False
    elif x == len_board and y == 0:
        if board[x-len_ship_to_place][y] == "S" and board[x-1][y] == "S":
            return True
        elif board[x][y+len_ship_to_place] == "S" and board[x][y+1] == "S":
            return True
        else:
            print("position the ship in a straight line")
            return False
    elif x == 0 and y == len_board:
        if board[x+len_ship_to_place][y] == "S" and board[x+1][y] == "S":
            return True
        elif board[x][y-len_ship_to_place] == "S" and board[x][y-1] == "S":
            return True
        else:
            print("position the ship in a straight line")
            return False
    elif x == len_board and y == len_board:
        if board[x-len_ship_to_place][y] == "S" and board[x-1][y] == "S":
            return True
        elif board[x][y-len_ship_to_place] == "S" and board[x][y-1] == "S":
            return True
        else:
            print("position the ship in a straight line")
            return False
    elif x == 0:
        if board[x+len_ship_to_place][y] == "S" and board[x+1][y] == "S":
            return True
        elif board[x][y-len_ship_to_place] == "S" and board[x][y-1] == "S":
            return True
        elif board[x][y+len_ship_to_place] == "S" and board[x][y+1] == "S":
            return True
        else:
            print("position the ship in a straight line")
            return False
    elif y == 0:
        if board[x-len_ship_to_place][y] == "S" and board[x-1][y] == "S":
            return True
        elif board[x+len_ship_to_place][y] == "S" and board[x+1][y] == "S":
            return True
        elif board[x][y+len_ship_to_place] == "S" and board[x][y+1] == "S":
            return True
        else:
            print("position the ship in a straight line")
            return False
    elif x == len_board:
        if board[x-len_ship_to_place][y] == "S" and board[x-1][y] == "S":
            return True
        elif board[x][y-len_ship_to_place] == "S" and board[x][y-1] == "S":
            return True
        elif board[x][y+len_ship_to_place] == "S" and board[x][y+1] == "S":
            return True
        else:
            print("position the ship in a straight line")
            return False
    elif y == len_board:
        if board[x-len_ship_to_place][y] == "S" and board[x-1][y] == "S":
            return True
        elif board[x+len_ship_to_place][y] == "S" and board[x+1][y] == "S":
            return True
        elif board[x][y-len_ship_to_place] == "S" and board[x][y-1] == "S":
            return True
        else:
            print("position the ship in a straight line")
            return False
    else:
        if loop_counter == 1:
            return True
        elif board[x-len_ship_to_place][y] == "S" and board[x-1][y] == "S":
            return True
        elif board[x+len_ship_to_place][y] == "S" and board[x+1][y] == "S":
            return True
        elif board[x][y-len_ship_to_place] == "S" and board[x][y-1] == "S":
            return True
        elif board[x][y+len_ship_to_place] == "S" and board[x][y+1] == "S":
            return True
        else:
            print("position the ship in a straight line")
            return False
# Krzysztof Bottom


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


def player_input_ships(board, amount_of_ships=2):
    n = 1
    while n <= amount_of_ships:
        place_ship(board, n)
        os.system("cls || clear")
        display_board(board)
        n += 1


def game(mode):
    board_size = get_board_size()
    board_player_1 = init_board(board_size)
    board_player_2 = init_board(board_size)
    current_player = Players.Player1
    print(f"Current player: {current_player}")
    display_board(board_player_1)
    player_amount_input = int(input("Provide number of ship: "))
    player_input_ships(board_player_1, player_amount_input)
    display_board(board_player_1)
    print("\n")
    current_player = Players.Player2
    print(f"Current player: {current_player}")
    display_board(board_player_2)
    player_amount_input = int(input("Provide number of ship: "))
    player_input_ships(board_player_2, player_amount_input)
    display_board(board_player_2)


    #Player 1 turn
    shot_attempt = get_coordinates()
    mark_move(shot_attempt[0], shot_attempt[1], board_player_1, board_player_2)
    display_two_boards(board_player_1, board_player_2)

if __name__ == "__main__":
    current_mode = Modes.HUMAN_HUMAN
    main_menu(current_mode)
