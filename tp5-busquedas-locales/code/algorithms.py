import random
import time
import math
from board import *
import numpy as np

def h_function(queens): #Contar ataques
    attacks = 0
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                attacks += 1
    return attacks

def hill_climbing(board, size, queens, max_steps=10000):
    current_attacks = h_function(queens)
    steps = 0
    h_history = [current_attacks]  # Iniciar la historia de H
    while steps < max_steps:
        steps += 1
        best_move = None
        best_attacks = current_attacks
        for i in range(size):
            original_row = queens[i][0]
            for j in range(size):
                if j == original_row:
                    continue
                new_queens = queens[:]
                new_queens[i] = (j, i)
                new_attacks = h_function(new_queens)
                if new_attacks < best_attacks:
                    best_attacks = new_attacks
                    best_move = (j, i)
        if best_move:
            queens[best_move[1]] = best_move
            current_attacks = best_attacks
            h_history.append(current_attacks)  # Actualizar historia de H
        else:
            break
        if current_attacks == 0:
            break
    return current_attacks == 0, steps, h_history

def simulated_annealing(board, size, queens, max_steps=10000, initial_temp=100, cooling_rate=0.99):
    current_attacks = h_function(queens)
    temperature = initial_temp
    steps = 0
    h_history = [current_attacks]
    while steps < max_steps and current_attacks > 0:
        steps += 1
        temperature *= cooling_rate
        col = random.randint(0, size - 1)
        old_row = queens[col][0]
        new_row = random.randint(0, size - 1)
        if old_row == new_row:
            continue
        new_queens = queens[:]
        new_queens[col] = (new_row, col)
        new_attacks = h_function(new_queens)
        delta_E = new_attacks - current_attacks
        if delta_E < 0 or random.random() < math.exp(-delta_E / temperature):
            queens[col] = (new_row, col)
            current_attacks = new_attacks
            h_history.append(current_attacks)
    return current_attacks == 0, steps, temperature, h_history

# --- Genetic Algorithm ---
def generate_population(size, population_size):  # Creo tableros de forma aleatoria
    population = []
    for _ in range(population_size):
        _, queens = generate_board(size)
        population.append(queens)
    return population

def mutate_board(queens, size):
    # Copiar la configuración de las reinas y hacer una mutación (intercambiar la posición de dos reinas)
    new_queens = queens[:]
    i, j = random.sample(range(size), 2)  # Elegir dos columnas al azar
    new_queens[i], new_queens[j] = new_queens[j], new_queens[i]  # Intercambiar las reinas
    return new_queens


def fitness_f(queens, size):
    total_pairs = (size * (size - 1)) // 2
    attacks = h_function(queens)
    fitness = total_pairs - attacks  # Cant pares - cant pares atacados = cant pares que no se atacan (fitness)
    return fitness

def selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    # Si todos los fitness son cero
    if total_fitness == 0:
        probabilities = [1 / len(fitnesses)] * len(fitnesses)
    else:
        probabilities = [f / total_fitness for f in fitnesses]
    selected = random.choices(population, weights=probabilities, k=2)
    return selected[0], selected[1]

def crossover(parent1, parent2, size):
    point = random.randint(1, size - 1)  # punto random
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutation(individual, size, mutation_rate=0.1):
    if random.random() < mutation_rate:
        col = random.randint(0, size - 1)  # Elegir una columna al azar
        row = random.randint(0, size - 1)  # Elegir una fila nueva al azar
        individual[col] = (row, individual[col][1])
    return individual

def genetic_algorithm(queens, size, population_size=100, max_generations=10000, mutation_rate=0.1):
    # Generar la población iniciald (reinas)
    population = [mutate_board(queens, size) for _ in range(population_size)]
    fitnesses = []
    for ind in population:
        fitnesses.append(fitness_f(ind, size))
    steps = 0
    for generation in range(max_generations):
        steps += 1
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2, size)
            new_population.extend([child1, child2])
        # Mutación
        new_population = [mutation(child, size, mutation_rate) for child in new_population]
        # nuevo fitness
        new_fitnesses = [fitness_f(ind, size) for ind in new_population]
        # Reemplazo (no elitista)
        population = new_population
        fitnesses = new_fitnesses
        if max(fitnesses) == (size * (size - 1)) // 2:  # Solución óptima
            return True, steps, generation
    # Si no se encontró una solución
    return False, steps, max_generations