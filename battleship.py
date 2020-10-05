from colorama import Fore, Back, Style

# INPUT
def get_move():
    x = True
    while x:
        move_input = input("please select place to fire in indicated order \"row\" \"col\":  ").upper()
        list_of_letter = list(map(chr,list(range(65,70))))
        list_of_number = list(map(str,list(range(1,6))))
        if move_input[0] not in list_of_letter:
            print("provide correct co-ordinates")   
        elif move_input[1] not in list_of_number:
            print("provide correct co-ordinates")     
        else:
            col = move_input[1]
            row = move_input[0]
            x= False

    return row, col


def get_ai_move():
    pass


# OUTPUT
def display_board(board):
    pass


def display_two_boards(board1, board2):
    pass


def display_logo():
    pass


def display_menu():
    pass


def display_mode_menu():
    pass


# LOGIC
def init_board(size=5):
    board= []
    row = []
    while len(board)<size:
        board.append(row) 
    while len(row)<size:
        row.append("0")
    return board

# bedzie problem z kolorem, wyprintowanie jednego zakolorowanego pola koloruje wszystko co jest później
# wrazie problemów https://pypi.org/project/colorama/  i zmiana wywoływania koloru.
#problem powienien byc zażegnany --> Style.RESET_ALL
def mark_move(row, col, board, enemy_board):
    if enemy_board[row][col] == "0":
        board[row][col]= Fore.BLACK + "V" + Style.RESET_ALL      
    elif enemy_board[row][col] == "S":
        board[row][col]= Fore.RED + "X" + Style.RESET_ALL    
    return board


def main_menu():
    pass


def mode_menu():
    pass


def game(mode):
    pass


if __name__ == "__main__":
    main_menu()
