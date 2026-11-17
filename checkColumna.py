def checkColumna(sudoku):
    n = len(sudoku)

    for columna in range(n):
        numeros = []

        for fila in range(n):
            numeros.append(sudoku[fila][columna])

        if sorted(numeros) != list(range(1, n + 1)):
            return False

    return True
