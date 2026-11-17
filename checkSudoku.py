# encoding: utf-8

from esCuadrado import esCuadrado
from checkcolumna import checkcolumna
from SonEnteros import SonEnteros
from checkfila import checkfila


# THREE GOLD STARS

correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

incorrecto1 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]

incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]

incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 6],
               [4, 5, 2, 1, 3],
               [3, 4, 5, 2, 1],
               [5, 6, 4, 3, 2]]

incorrecto4 = [['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]

incorrecto5 = [[1, 1.5],
               [1.5, 1]]

incorrecto6 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]


def check_sudoku(sudoku):

    if not esCuadrado(sudoku):
        return False

    if not SonEnteros(sudoku):
        return False

    if not checkfila(sudoku):
        return False

    if not checkcolumna(sudoku):
        return False

    return True


# Casos test

print(check_sudoku(incorrecto1))
# >>> False

print(check_sudoku(correcto))
# >>> True

print(check_sudoku(incorrecto2))
# >>> False

print(check_sudoku(incorrecto3))
# >>> False

print(check_sudoku(incorrecto4))
# >>> False

print(check_sudoku(incorrecto5))
# >>> False

print(check_sudoku(incorrecto6))
# >>> False
