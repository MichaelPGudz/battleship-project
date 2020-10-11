import string


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


def get_ai_move():
    pass


def display_select_ship_menu(current_player):
    print(current_player)


def is_empty_field(board, user_input):
    row, col = convert_input_to_coordinates(user_input)
    if board[row][col] == '0':
        return True
    return False
