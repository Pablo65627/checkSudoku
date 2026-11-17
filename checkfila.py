def checkfila(sudoku):
    n = len(sudoku)
    numeros = set(range(1, n + 1))

    for fila in sudoku:
        if set(fila) != numeros:
            return False

    return True
