def SonEnteros(sudoku):
    for fila in sudoku:
        for numero in fila:
            if not isinstance(numero, int) or isinstance(numero, bool):
                return False

    return True
