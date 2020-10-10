import Output
import os
import string
from enums import Players, Modes
from colorama import Fore, Style


# INPUT
def convert_input_to_coordinates(user_input):
    """Convert input e.g. A1 to indexes of 2 dimension board."""
    row = user_input[0]
    col = int(user_input[1:])
    row = string.ascii_uppercase.index(row)
    col -= 1
    return row, col


def get_move(board, is_setting_ships=True):
    """Get move from user e.g. A1, if input is not correct ask again."""
    board_size = len(board)
    row_headers = list(map(lambda x: x + 1, list(range(board_size))))
    row_headers = [str(element) for element in row_headers]
    col_headers = string.ascii_uppercase[:board_size]

    user_input = input("Provide coordinates (e.g. A1): ").upper()
    if is_setting_ships:
        while user_input[0] not in col_headers or \
                user_input[1] not in row_headers or \
                not is_empty_field(board, user_input):
            user_input = input("Please try again. Provide coordinates (e.g. A1): ").upper()
    else:
        while user_input[0] not in col_headers or \
                user_input[1] not in row_headers:
            user_input = input("Please try again. Provide coordinates (e.g. A1): ").upper()
    return convert_input_to_coordinates(user_input)


def get_board_size():
    """Function in which player defines the size of the grid. It also checks input to be digit."""
    board_size = input("Please enter number of columns in the board: \n")
    while not board_size.isdigit() or int(board_size) < 5 or int(board_size) > 10:
        board_size = input("Wrong value, please try again!")
    return int(board_size)


def get_coordinates(ship_size=None, board_size=5):
    assignment_bool = True
    while assignment_bool:
        move_input = input(f"Provide coordinates in indicated order "
                           f"\"row\" \"col\" (ship size: {ship_size}): ").upper()
        list_of_letter = list(map(chr, list(range(65, (board_size + 65)))))
        list_of_number = list(map(str, list(range(1, (board_size + 1)))))
        if move_input[0] not in list_of_letter or move_input[1] not in list_of_number:
            print("Provide correct coordinates!")
        else:
            row = translate_row(move_input[0], list_of_letter, list_of_number)
            col = int(move_input[1:]) - 1
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


def is_empty_field(board, user_input):
    row, col = convert_input_to_coordinates(user_input)
    if board[row][col] == '0':
        return True
    return False


def place_ship(board, ship_len=1):
    part_of_ship = 0
    while ship_len > part_of_ship:
        os.system("cls || clear")
        Output.display_board(board)
        row, col = get_coordinates()
        part_of_ship += 1
        while not is_next(board, row, col, part_of_ship):
            row, col = get_coordinates()
        board[row][col] = 'S'
    return board


def is_part_of_ship(board, row, col, part_of_ship):
    ship_mark = 'X'
    if part_of_ship == 1:
        return True

    if board[row - part_of_ship][col] == ship_mark and board[row - 1][col] == ship_mark:
        return True
    elif board[x + len_ship_to_place][y] == "S" and board[x + 1][y] == "S":
        return True
    elif board[x][y - len_ship_to_place] == "S" and board[x][y - 1] == "S":
        return True
    elif board[x][y + len_ship_to_place] == "S" and board[x][y + 1] == "S":
        return True
    return False


def is_next(board, x, y, part_of_ship):
    len_board = len(board) - 1
    len_ship_to_place = part_of_ship - 1
    communicate = "Place the ship in a straight line!"
    ship_mark = "X"
    if part_of_ship == 1:
        return True
    elif x == 0 and y == 0:
        if board[x + len_ship_to_place][y] == ship_mark and board[x + 1][y] == ship_mark:
            return True
        elif board[x][y + len_ship_to_place] == ship_mark and board[x][y + 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif x == len_board and y == 0:
        if board[x - len_ship_to_place][y] == ship_mark and board[x - 1][y] == ship_mark:
            return True
        elif board[x][y + len_ship_to_place] == ship_mark and board[x][y + 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif x == 0 and y == len_board:
        if board[x + len_ship_to_place][y] == ship_mark and board[x + 1][y] == ship_mark:
            return True
        elif board[x][y - len_ship_to_place] == ship_mark and board[x][y - 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif x == len_board and y == len_board:
        if board[x - len_ship_to_place][y] == ship_mark and board[x - 1][y] == ship_mark:
            return True
        elif board[x][y - len_ship_to_place] == ship_mark and board[x][y - 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif x == 0:
        if board[x + len_ship_to_place][y] == ship_mark and board[x + 1][y] == ship_mark:
            return True
        elif board[x][y - len_ship_to_place] == ship_mark and board[x][y - 1] == ship_mark:
            return True
        elif board[x][y + len_ship_to_place] == ship_mark and board[x][y + 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif y == 0:
        if board[x - len_ship_to_place][y] == ship_mark and board[x - 1][y] == ship_mark:
            return True
        elif board[x + len_ship_to_place][y] == ship_mark and board[x + 1][y] == ship_mark:
            return True
        elif board[x][y + len_ship_to_place] == ship_mark and board[x][y + 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif x == len_board:
        if board[x - len_ship_to_place][y] == ship_mark and board[x - 1][y] == ship_mark:
            return True
        elif board[x][y - len_ship_to_place] == ship_mark and board[x][y - 1] == ship_mark:
            return True
        elif board[x][y + len_ship_to_place] == ship_mark and board[x][y + 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    elif y == len_board:
        if board[x - len_ship_to_place][y] == ship_mark and board[x - 1][y] == ship_mark:
            return True
        elif board[x + len_ship_to_place][y] == ship_mark and board[x + 1][y] == ship_mark:
            return True
        elif board[x][y - len_ship_to_place] == ship_mark and board[x][y - 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False
    else:
        if part_of_ship == 1:
            return True
        elif board[x - len_ship_to_place][y] == ship_mark and board[x - 1][y] == ship_mark:
            return True
        elif board[x + len_ship_to_place][y] == ship_mark and board[x + 1][y] == ship_mark:
            return True
        elif board[x][y - len_ship_to_place] == ship_mark and board[x][y - 1] == ship_mark:
            return True
        elif board[x][y + len_ship_to_place] == ship_mark and board[x][y + 1] == ship_mark:
            return True
        else:
            print(communicate)
            return False


def get_ai_move():
    pass


def display_select_ship_menu(current_player):
    print(current_player)


# LOGIC
def main_menu(mode):
    Output.display_menu(mode)
    user_input = input("Your pick: ")
    choices = ['1', '2', '3']
    while user_input not in choices:
        user_input = input('Incorrect value. Your pick: ')

    if user_input == '1':
        game(mode)
    elif user_input == '2':
        Output.display_mode_menu()
        mode_menu(mode)
    elif user_input == '3':
        print()
        print("Good bye! See you next time.")
        input("Press enter to continue...")


def mode_menu(mode):
    Output.display_mode_menu()
    user_input = input("Your pick: ").lower()
    choices = ['1', '2', 'back']
    while user_input not in choices:
        user_input = input('Incorrect value. Your pick: ').lower()
    if user_input == '1':
        mode = Modes.HUMAN_HUMAN
        main_menu(mode)
    elif user_input == '2':
        mode = Modes.HUMAN_AI
        main_menu(mode)
    elif user_input == 'back':
        Output.display_menu(mode)
        main_menu(mode)


def init_board(size=5):
    board = []
    row = []
    while len(row) < size:
        row.append("0")
    while len(board) < size:
        copy_row = row.copy()
        board.append(copy_row)
    return board


def player_input_ships(board, amount_of_ships=2):
    n = 1
    while n <= amount_of_ships:
        place_ship(board, n)
        n += 1


def enter_ships(player, board_size=5, ship_amount=2):
    """Function initialize board object for the provided player and asks for the location of the ships on the grid"""
    os.system("cls || clear")
    player_board = init_board(board_size)
    print("Set your ships!\n")
    Output.display_board(player_board)
    print(f"\nCurrent player: {str(player).split('.')[1]}")
    player_input_ships(player_board, ship_amount)
    Output.display_board(player_board)
    print("\n")
    return player_board


# wrazie problemów https://pypi.org/project/colorama/  i zmiana wywoływania koloru.
def mark_move(row, col, board, enemy_board):
    if enemy_board[row][col] == "0":
        board[row][col] = Fore.BLACK + "V" + Style.RESET_ALL
        # enemy_board[row][col] = Fore.BLACK + "V" + Style.RESET_ALL
    elif enemy_board[row][col] == "S":
        board[row][col] = Fore.RED + "X" + Style.RESET_ALL
        # enemy_board[row][col] = Fore.BLACK + "X" + Style.RESET_ALL
    return board


def has_won(player):
    """Return True if player won."""
    return False


def game(mode):
    board_player_1 = enter_ships(Players.Player1)
    board_player_1_enemy = init_board()
    board_player_2 = enter_ships(Players.Player2)
    board_player_2_enemy = init_board()

    players_boards = {Players.Player1: board_player_1, Players.Player2: board_player_2}
    players = list(players_boards.keys())
    current_player = list(players_boards.keys())[0]

    # while not has_won(current_player):

    # Player 1 turn
    # Output.display_two_boards(board_player_1_enemy, board_player_2_enemy)
    # print(f"{Players.Player1} turn", end="\n")
    # shot_attempt = get_coordinates()
    # mark_move(shot_attempt[0], shot_attempt[1], board_player_1_enemy, board_player_2)
    # # display_board(board_player_1_enemy)
    # amount_of_hits_player_1 = sum(x.count("\x1b[31mX\x1b[0m") for x in board_player_1_enemy)
    # amount_of_ships_player_2 = sum(x.count("S") for x in board_player_2)
    # print(amount_of_hits_player_1, amount_of_ships_player_2)
    #
    # # Player 2 Turn
    # print(f"{Players.Player2} turn", end="\n")
    # shot_attempt = get_coordinates()
    # mark_move(shot_attempt[0], shot_attempt[1], board_player_2_enemy, board_player_1)
    # # display_board(board_player_2_enemy)
    # amount_of_hits_player_2 = sum(x.count("\x1b[31mX\x1b[0m") for x in board_player_2_enemy)
    # amount_of_ships_player_1 = sum(x.count("S") for x in board_player_1)
    # print(amount_of_hits_player_2, amount_of_ships_player_1)
    # check_empty_spaces_player_1 = sum(x.count("0") for x in board_player_2_enemy)
    # check_empty_spaces_player_2 = sum(x.count("0") for x in board_player_1_enemy)

    # if amount_of_hits_player_1 == amount_of_ships_player_2:
    #     print("Player 1 has won!")
    #     has_won = True
    # elif amount_of_hits_player_2 == amount_of_ships_player_1:
    #     print("Player 2 has won!")
    #     has_won = True
    # elif check_empty_spaces_player_1 == 0 or check_empty_spaces_player_2 == 0:
    #     print("It's a tie")
    #     has_won = True


if __name__ == "__main__":
    current_mode = Modes.HUMAN_HUMAN
    main_menu(current_mode)
