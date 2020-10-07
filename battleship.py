from colorama import Fore, Back, Style

get_move_text = "please select place to fire in indicated order \"row\" \"col\":  "
palece_ship_text= "pleace select place for you ship "

# INPUT
def get_coordinates(text):
    x = True
    while x:
        move_input = input(text).upper()
        list_of_letter = list(map(chr,list(range(65,70))))
        list_of_number = list(map(str,list(range(1,6))))
        if move_input[0] not in list_of_letter:
            print("provide correct coordinates")   
        elif move_input[1] not in list_of_number:
            print("provide correct coordinates")     
        else:
            row_translator = {"A": 0 , "B" : 1 , "C":2, "D": 3, "E" :4 }
            row = row_translator[move_input[0]]
            col = move_input[1]-1
            x= False

    return row, col


def place_ship(board):
    x = True
    while x : 
        x,y = get_coordinates(palece_ship_text)

        if board[x][y] == "0":
            board[x][y] = "S"
            print(f"place {x},{y} has been taken")
            x= False
        else:
            print("provide empty coordinates")
    return board


def is_next(board):
     

    pass



    
        

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
        enemy_board[row][col]= Fore.BLACK + "V" + Style.RESET_ALL       
    elif enemy_board[row][col] == "S":
        board[row][col]= Fore.RED + "X" + Style.RESET_ALL 
        enemy_board[row][col]= Fore.BLACK + "X" + Style.RESET_ALL    
    return board


def main_menu():
    pass


def mode_menu():
    pass


def game(mode):
    pass


if __name__ == "__main__":
    main_menu()
