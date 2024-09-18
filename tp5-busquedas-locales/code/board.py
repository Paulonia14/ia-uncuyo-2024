import random

def generate_board(size):
    queens = []
    mat = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):  # Por cada columna pone una reina
        x = random.randint(0, size - 1)
        mat[x][i] = 1
        queens.append((x, i))
    return mat, queens