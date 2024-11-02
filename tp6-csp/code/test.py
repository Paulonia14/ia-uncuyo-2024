import random
def create_empty_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]

def is_safe(queens, row, col):
    for i in range(row):
        # Misma columna
        if queens[i] == col:
            return False
        # Diagonales
        if abs(queens[i] - col) == abs(i - row):
            return False
    return True

def solve_N_queens(board, queens, row, size):
    if row == size:  # Caso base: todas las reinas están colocadas
        return True
    for col in range(size):
        if is_safe(queens, row, col):
            queens[row] = col  # Colocar reina
            board[row][col] = 1  # Marcar en el board
            if solve_N_queens(board, queens, row + 1, size):
                return True
            # Backtracking
            queens[row] = -1
            board[row][col] = 0
    return False

def CSP_backtracking(size):
    board = create_empty_board(size)
    queens = [-1] * size  # Inicializa la lista de reinas con -1
    print("a")
    print(queens)
    print("a")
    if solve_N_queens(board, queens, 0, size):
        print("Solución encontrada:")
        print(board)
    else:
        print("No hay solución.")

# Ejemplo para 8 reinas

CSP_backtracking(4)
