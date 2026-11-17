def checkFila(sudoku):
    n = len(sudoku)

    for fila in sudoku:
        if sorted(fila) != list(range(1, n + 1)):
            return False

    return True
