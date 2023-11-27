# Mostrar tablero

def display_board(board):
    print(f'{board[6]} | {board[7]} | {board[8]}')
    print('--|---|--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--|---|--')
    print(f'{board[0]} | {board[1]} | {board[2]}')
    return board

# Decidir si jugar o no

def replay():
    play = input ("Quieres continuar juagando Y o N? ")
    while play != "N" and play != "Y":
        play = input ("Quieres continuar juagando Y o N? ")
    return play
    

#Elegir jugador

def player_input(player_marker):
    while player_marker != "X" and player_marker != "O":
        player_marker = input ("Elige tu marca de jugador X o O: ")
    return player_marker

#Marcar casilla solo si vacia

def place_marker(board, player_marker, position):
    while position not in ["1","2","3","4","5","6","7","8","9"]:
        position = input("Elige una posición del 1 al 9: ")
    else:
        position = int(position)
        while board[position-1] == "X" or board[position-1] == "O":
            print ("Esa casilla ya está ocupada")
            position = int(input("Elige una posición del 1 al 9: "))
        board[position-1] = player_input(player_marker)
        
def win_check(board, player_marker):
    if board[0] == board[1] == board[2] != " ":
        print ("you win")
        return True
    elif board[3] == board[4] == board[5] != " ":
        print ("you win") 
        return True
    elif board[6] == board[7] == board[8] != " ":
        print ("you win")
        return True
    elif board[0] == board[4] == board[8] != " ":
        print ("you win")
        return True 
    elif board[6] == board[4] == board[2] != " ":
        print ("you win")
        return True
    else: 
        return False
 
 
board = [" "]*9
player_marker = 5
position = 0
        
display_board(board)
player_input(player_marker)
while win_check(board, player_marker) == False:
    
    place_marker(board, player_marker, position)
    display_board(board)