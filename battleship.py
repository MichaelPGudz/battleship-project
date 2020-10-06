import os, string
from bs_cursor import Cursor


# INPUT
def get_move(player):
    pass


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
    pass


def mark_move(board, sign='X'):
    pass


def main_menu():
    user_input = input("Your pick: ")
    choices = ['1', '2', '3']
    while user_input not in choices:
        user_input = input('Incorrect value. Your pick: ')

    if user_input == '1':
        # TODO change mode on enum
        game('mode')
    elif user_input == '2':
        display_mode_menu()
        mode_menu()
    elif user_input == '3':
        print()
        print("Good bye! See you next time.")
        input("Press enter to continue...")


def mode_menu(mode):
    user_input = input("Your pick: ").lower()
    choices = ['1', '2', 'back']
    while user_input not in choices:
        user_input = input('Incorrect value. Your pick: ').lower()
    # TODO change mode on enum
    if user_input == '1':
        mode = 'HUMAN_HUMAN'
    elif user_input == '2':
        mode = 'HUMAN_AI'
    elif user_input == 'back':
        display_menu()
        main_menu()


def game(mode):
    pass


if __name__ == "__main__":
    main_menu()
