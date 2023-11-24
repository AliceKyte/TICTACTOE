"""
Mostrar lista
Pedir al usuario que seleccione una posición
Pedir al usuario que indique que escribir en la posición
Mostrar resultado
Preguntar si continua jugando
"""

# Mostrar tablero

row0 = "  1    2    3 "
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

def display(row1, row2, row3):
    print(f' {row0}')
    print(f'A{row1}')
    print(f'B{row2}')
    print(f'C{row3}')

#  Pedir al usuario que seleccione una columna
def colum_choose():
    selection = "none"
    rango_deseado = [1, 2, 3]
    while selection.isdigit() == False:
        selection = input('Selecciona un número entre (1, 2 y 3): ')
        if selection.isdigit():
            selection = int(selection)
        
            if selection not in rango_deseado:
                selection = "none"
            else:
                return int(selection)
        else:
            selection = "none"
            
#  Pedir al usuario que seleccione una fila

def row_choose():
    selection_row = "none"
    rango_deseado = ["A", "B", "C"]
    while selection_row != "A" and selection_row != "B" and selection_row !="C":
        selection_row = input('Selecciona una fila entre (A, B y C): ')
        if selection_row == "A":
            return row1
        elif selection_row == "B":
            return row2
        elif selection_row == "C":
            return row3
        else:
            selection_row = "none"

# Pedir al usuario que indique que escribir en la posición
            
def user_write():
    write = " "
    while write != "O" and write != "X":
        write = input ("Indica tu ficha de jugador (O - X) ")
    return write

# Preguntar si continua jugando

def continue_playin(display):
    continue_p = False
    while continue_p == False:
        continue_p = input ("Quieres seguir jugando (Y o N)? ")
        if continue_p != "N" and continue_p != "Y":
            pass
        elif continue_p == "N":
            print("Gracias por su participación")
            row1 = [" ", " ", " "]
            row2 = [" ", " ", " "]
            row3 = [" ", " ", " "]
        elif continue_p == "Y":
            return True
        else:
            pass
    
    
# Ejecucíon de la secuencia de juego

    def result_round(display, colum_choose, user_write):
        while continue_playin(display):
            display(row1, row2, row3)
            position = colum_choose()-1
            fila = row_choose()
            fila[position] = user_write()
            display(row1, row2, row3)