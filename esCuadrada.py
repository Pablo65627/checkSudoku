def esCuadrada(sudoku):
    n = len(sudoku)

    for fila in sudoku:
        if len(fila) != n:
            return False

    return True
