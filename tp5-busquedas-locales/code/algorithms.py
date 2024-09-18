import random
import time
import math
from board import *

def h_function(queens):
    attacks = 0
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                attacks += 1
    return attacks


def hill_climbing(board, size, queens, max_steps=1000):
    current_attacks = h_function(queens)
    steps = 0
    while steps < max_steps:
        steps += 1
        best_move = None
        best_attacks = current_attacks
        for i in range(size):
            for j in range(size):
                if board[j][i] == 1:  # Si hay una reina
                    continue
                new_queens = queens[:]
                new_queens[i] = (j, i)  # Mueve reina
                new_attacks = h_function(new_queens)
                if new_attacks < best_attacks:
                    best_attacks = new_attacks
                    best_move = (j, i)
        if best_move:
            queens[best_move[1]] = best_move
            current_attacks = best_attacks
        else:
            break
        if current_attacks == 0:
            break
    return current_attacks == 0, steps

def simulated_annealing(board, size, queens, max_steps=1000, initial_temp=100, cooling_rate=0.99):
    current_attacks = h_function(queens)
    temperature = initial_temp
    steps = 0
    while steps < max_steps and current_attacks > 0:
        steps += 1
        temperature *= cooling_rate
        col = random.randint(0, size - 1)
        old_row = queens[col][0]
        new_row = random.randint(0, size - 1)
        board[old_row][col] = 0
        board[new_row][col] = 1
        queens[col] = (new_row, col)
        new_attacks = h_function(queens)
        if new_attacks < current_attacks:  # Si mejora nuevo mov, aceptamos
            current_attacks = new_attacks
        else:
            # Si no mejora
            probabilidad = math.exp((current_attacks - new_attacks) / temperature)
            if random.uniform(0, 1) >= probabilidad:  # No aceptamos (revertir cambio)
                board[new_row][col] = 0
                board[old_row][col] = 1
                queens[col] = (old_row, col)
    return board, current_attacks, steps