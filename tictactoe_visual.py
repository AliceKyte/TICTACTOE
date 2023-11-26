from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("TICTACTOE")
ventana.config(
    bd=15,
    bg="#ecb9ed"
)
marco = Frame(ventana).grid()

# Mostrar tablero

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player_marker = 5
position = 0

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
    
    while board[position-1] == "X" or board[position-1] == "O":
        print ("Esa casilla ya está ocupada")
        position = int(input("Elige una posición del 1 al 9: "))
            
    board[position-1] = player_input(player_marker)
    
    


        
#--------------- primera linea de ventanas -----------------------


your_try= StringVar() 
your_try.set(player_marker)

pantalla7 = Entry(marco, textvariable = your_try, width=3, bg="#7df5db", fg="#7df5db", justify="center")
pantalla7.grid(row=4, column=0, padx=5, pady=5)
'''
boton8 = Button(marco,  text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 8))
boton8.grid(row=1, column=1, padx=5, pady=5)
boton9 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 9))
boton9.grid(row=1, column=2, padx=5, pady=5)

#--------------- segunda linea de ventanas -----------------------

boton4 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 4))
boton4.grid(row=2, column=0, padx=5, pady=5)
boton5 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 5))
boton5.grid(row=2, column=1, padx=5, pady=5)
boton6 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 6))
boton6.grid(row=2, column=2, padx=5, pady=5)


#--------------- tercera linea de ventanas -----------------------

boton1 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 1))
boton1.grid(row=3, column=0, padx=5, pady=5)
boton2 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 2))
boton2.grid(row=3, column=1, padx=5, pady=5)
boton3 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 3))
boton3.grid(row=3, column=2, padx=5, pady=5)
'''
#---------------------------------------------------------------------------------------------------------------#

boton7 = Button(marco, text="",  width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 7))
boton7.grid(row=1, column=0, padx=5, pady=5)
boton8 = Button(marco,  text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 8))
boton8.grid(row=1, column=1, padx=5, pady=5)
boton9 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 9))
boton9.grid(row=1, column=2, padx=5, pady=5)

#--------------- segunda linea de botones -----------------------

boton4 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 4))
boton4.grid(row=2, column=0, padx=5, pady=5)
boton5 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 5))
boton5.grid(row=2, column=1, padx=5, pady=5)
boton6 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 6))
boton6.grid(row=2, column=2, padx=5, pady=5)


#--------------- tercera linea de botones -----------------------

boton1 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 1))
boton1.grid(row=3, column=0, padx=5, pady=5)
boton2 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 2))
boton2.grid(row=3, column=1, padx=5, pady=5)
boton3 = Button(marco, text="", width=3, bg= "#7df5db", command = lambda: place_marker(board, player_marker, 3))
boton3.grid(row=3, column=2, padx=5, pady=5)


ventana.mainloop()

display_board(board)
place_marker(board, player_marker, position)
display_board(board)
place_marker(board, player_marker, position)
display_board(board)
place_marker(board, player_marker, position)
display_board(board)
place_marker(board, player_marker, position)
display_board(board)
place_marker(board, player_marker, position)
display_board(board)
place_marker(board, player_marker, position)
display_board(board)
