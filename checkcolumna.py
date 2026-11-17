def checkcolumna(sudoku):
    n = len(sudoku)
    numeros = set(range(1, n + 1))

    for columna in range(n):
        valores = set()

        for fila in range(n):
            valores.add(sudoku[fila][columna])

        if valores != numeros:
            return False

    return True
