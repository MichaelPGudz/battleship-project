from colorama import Fore, Back, Style


# INPUT
def get_coordinates(size=5):
    
    assignment_bool = True
    while assignment_bool:
        move_input = input("please select coordinates in indicated order \"row\" \"col\"").upper()
        list_of_letter = list(map(chr,list(range(65,65+size))))
        list_of_number = list(map(str,list(range(1,1+size))))
        if move_input[0] not in list_of_letter or move_input[1] not in list_of_number:
            print("provide correct coordinates")      
        else:
            row =  translate_row(move_input[0],list_of_letter,list_of_number)
            col = int(move_input[1])-1
            assignment_bool = False

    return row, col


def translate_row(row,list_of_letter,list_of_number):
    list_len = len(list_of_number)
    list_of_number.insert(0,"0")
    list_of_number.remove(str(list_len))

    row_translator = {}
    for key in list_of_letter: 
        for value in list_of_number: 
            row_translator[key] = value 
            list_of_number.remove(value) 
            break
    
    coordinate_x = row_translator[row]

    return int(coordinate_x)


def place_ship(board,ship_len=1):
    
   
    while_loop_counter=0
    while ship_len>while_loop_counter:
        assignment_bool = True
        while_loop_counter+=1
        while assignment_bool : 
            row,col = get_coordinates()
            is_next_bool = is_next(board,row,col,while_loop_counter,ship_len)
            
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


def is_next(board,x,y,loop_counter,ship_len=1):
    len_board =len(board)-1
    len_ship_to_place = loop_counter -1
    if loop_counter == 1 :
        return True 
    elif x == 0 and y==0:
        if board[x+len_ship_to_place][y]=="S" and board[x+1][y]=="S":
            return True
        elif board[x][y+len_ship_to_place]=="S" and board[x][y+1]=="S":
            return True
        else:
            print("position the ship in a straight line")
            return False
    elif x == len_board and y==0 :
        if board[x-len_ship_to_place][y]=="S" and board[x-1][y]=="S":
            return True
        elif board[x][y+len_ship_to_place]=="S" and board[x][y+1]=="S":
            return True
        else:
            print("position the ship in a straight line")
            return False        
    elif x == 0 and y == len_board:
        if board[x+len_ship_to_place][y]=="S" and board[x+1][y]=="S":
            return True
        elif board[x][y-len_ship_to_place]=="S" and board[x][y-1]=="S":
            return True
        else:
            print("position the ship in a straight line")
            return False
    elif x == len_board and y == len_board:
        if board[x-len_ship_to_place][y]=="S" and board[x-1][y]=="S":
            return True
        elif board[x][y-len_ship_to_place]=="S" and board[x][y-1]=="S":
            return True
        else:
            print("position the ship in a straight line")
            return False
    elif x == 0 :
        if board[x+len_ship_to_place][y]=="S" and board[x+1][y]=="S":
            return True
        elif board[x][y-len_ship_to_place]=="S" and board[x][y-1]=="S":
            return True
        elif board[x][y+len_ship_to_place]=="S" and board[x][y+1]=="S":
            return True            
        else:
            print("position the ship in a straight line")
            return False
    elif y==0 :
        if board[x-len_ship_to_place][y]=="S" and board[x-1][y]=="S":
            return True
        elif board[x+len_ship_to_place][y]=="S" and board[x+1][y]=="S":
            return True
        elif board[x][y+len_ship_to_place]=="S" and board[x][y+1]=="S":
            return True
        else:
            print("position the ship in a straight line")
            return False
    elif x== len_board :
        if board[x-len_ship_to_place][y]=="S" and board[x-1][y]=="S" :
            return True
        elif board[x][y-len_ship_to_place]=="S" and board[x][y-1]=="S":
            return True
        elif board[x][y+len_ship_to_place]=="S" and board[x][y+1]=="S":
            return True            
        else:
            print("position the ship in a straight line")
            return False
    elif y == len_board :
        if board[x-len_ship_to_place][y]=="S"  and board[x-1][y]=="S":
            return True
        elif board[x+len_ship_to_place][y]=="S" and board[x+1][y]=="S":
            return True
        elif board[x][y-len_ship_to_place]=="S" and board[x][y-1]=="S":
            return True
        else:
            print("position the ship in a straight line")
            return False
    else:
        if loop_counter == 1 :
            return True         
        elif board[x-len_ship_to_place][y]=="S" and board[x-1][y]=="S" :
            return True
        elif board[x+len_ship_to_place][y]=="S" and board[x+1][y]=="S" :
            return True
        elif board[x][y-len_ship_to_place]=="S" and  board[x][y-1]=="S":
            return True
        elif board[x][y+len_ship_to_place]=="S" and board[x][y+1]=="S":
            return True
        else:
            print("position the ship in a straight line")
            return False
               
    

        



    
        

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
    while len(row)<size:
        row.append("0")
    while len(board)<size:
        copy_row = row.copy()
        board.append(copy_row) 
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
