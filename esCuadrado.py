def esCuadrado(sudoku):
    n = len(sudoku)

    if n == 0:
        return False

    for fila in sudoku:
        if len(fila) != n:
            return False

    return True
