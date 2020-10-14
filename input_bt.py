import string
import time
import random


def convert_input_to_coordinates(user_input):
    """Convert input e.g. A1 to indexes of 2 dimension board."""
    row = user_input[0]
    col = int(user_input[1])
    row = string.ascii_uppercase.index(row)
    col -= 1
    return row, col


def get_move(board, is_setting_ships=True, additional_message=""):
    """Get move from user e.g. A1, if input is not correct ask again."""
    board_size = len(board)
    row_headers = list(map(lambda x: x + 1, list(range(board_size))))
    row_headers = [str(element) for element in row_headers]
    col_headers = string.ascii_uppercase[:board_size]

    user_input = input(F"Provide coordinates (e.g. A1){additional_message}: ").upper()
    if is_setting_ships:
        while len(user_input) < 2 or\
                user_input[0] not in col_headers or \
                user_input[1] not in row_headers or \
                not is_empty_field(board, user_input):
            user_input = input("Incorrect coordinates. Provide coordinates (e.g. A1){additional_message}: ").upper()
    else:
        while len(user_input) < 2 or\
                user_input[0] not in col_headers or \
                user_input[1] not in row_headers:
            user_input = input("Incorrect coordinates. Provide coordinates (e.g. A1){additional_message}: ").upper()
    return convert_input_to_coordinates(user_input)


def ai_shoot(board, fields_checked, ships_hit):
    """Gets move from AI."""
    board_size = len(board)
    row_headers = list(map(lambda x: x + 1, list(range(board_size))))
    row_headers = [str(element) for element in row_headers]
    col_headers = string.ascii_uppercase[:board_size]
    board_fields = {"columns": col_headers, "rows": row_headers}
    # try:
    #     x, y = convert_input_to_coordinates(fields_checked[-1])
    #     if board[x][y] == 'S':
    #         ships_hit.add(fields_checked[-1])
    #         try:
    #             col_guess = string.ascii_uppercase[y + random.randint(-1, 1)]
    #             row_guess = x + random.randint(-1, 1)
    #             field_guess = col_guess + str(row_guess)
    #             while field_guess in fields_checked:
    #                 print("Already in! Let's try again!")
    #                 col_guess = string.ascii_uppercase[y + random.randint(-1, 1)]
    #                 row_guess = x + random.randint(-1, 1)
    #                 field_guess = col_guess + str(row_guess)
    #         except ValueError:
    #             pass
    # except IndexError:
    #     pass
    col_guess = random.choice(board_fields["columns"])
    row_guess = random.choice(board_fields["rows"])
    field_guess = col_guess + str(row_guess)
    while field_guess in fields_checked:
        print("Already in! Let's try again!")
        col_guess = random.choice(board_fields["columns"])
        row_guess = random.choice(board_fields["rows"])
        field_guess = col_guess + str(row_guess)

    fields_checked.append(field_guess)
    print(fields_checked)
    time.sleep(1.0)
    return convert_input_to_coordinates(field_guess)

def get_ai_move(player, board_size=5, ship_size=2):
    pass


def display_select_ship_menu(current_player):
    print(current_player)


def is_empty_field(board, user_input):
    row, col = convert_input_to_coordinates(user_input)
    if board[row][col] == '0':
        return True
    return False
