def SonEnteros(sudoku):
    for fila in sudoku:
        for numero in fila:
            if type(numero) != int:
                return False

    return True
