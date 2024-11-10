import time
import csv
import random
import plot
from board import generate_board
import algorithms
import pandas as pd

def run_experiment(sizes=[4, 8, 10], runs=30, filename='results.csv'):
    results = []
    time_data = {'Simulated Annealing': [], 'Hill Climbing': [], 'Genetic Algorithm': [], 'CSP Backtracking': [], 'CSP Forward Checking': []}
    steps_data = {'Simulated Annealing': [], 'Hill Climbing': [], 'Genetic Algorithm': [], 'CSP Backtracking': [], 'CSP Forward Checking': []}
    success_data = {'Simulated Annealing': [], 'Hill Climbing': [], 'Genetic Algorithm': [], 'CSP Backtracking': [], 'CSP Forward Checking': []}
    all_time_data = {'Simulated Annealing': [], 'Hill Climbing': [], 'Genetic Algorithm': [], 'CSP Backtracking': [], 'CSP Forward Checking': []}
    all_steps_data = {'Simulated Annealing': [], 'Hill Climbing': [], 'Genetic Algorithm': [], 'CSP Backtracking': [], 'CSP Forward Checking': []}

    for size in sizes:
        for algorithm in ['Simulated Annealing', 'Hill Climbing', 'Genetic Algorithm', 'CSP Backtracking', 'CSP Forward Checking']:
            successes = 0
            times = []
            steps_list = []

            for _ in range(runs):
                board, queens = generate_board(size)
                start_time = time.time()

                # Seleccionar el algoritmo
                if algorithm == 'Simulated Annealing':
                    solution_found, steps, _, _ = algorithms.simulated_annealing(board, size, queens)
                elif algorithm == 'Hill Climbing':
                    solution_found, steps, _ = algorithms.hill_climbing(board, size, queens)
                elif algorithm == 'Genetic Algorithm':
                    solution_found, steps, _ = algorithms.genetic_algorithm(queens, size)
                elif algorithm == 'CSP Backtracking':
                    solution_found, steps, exec_time = algorithms.CSP_backtracking(queens, size)
                elif algorithm == 'CSP Forward Checking':
                    solution_found, steps, exec_time = algorithms.CSP_forward(queens, size)

                # Calcular el tiempo de ejecución si no se ha calculado dentro del algoritmo
                exec_time = time.time() - start_time if 'exec_time' not in locals() else exec_time
                times.append(exec_time)
                steps_list.append(steps)

                # Actualizar contadores si se encontró una solución óptima
                if solution_found:
                    successes += 1

            # Almacenar datos adicionales para estadísticas finales
            all_time_data[algorithm].extend(times)
            all_steps_data[algorithm].extend(steps_list)

            # Guardar resultados en la lista de resultados
            success_rate = (successes / runs) * 100
            avg_time = sum(times) / runs
            avg_steps = sum(steps_list) / runs
            std_time = (sum([(t - avg_time) ** 2 for t in times]) / runs) ** 0.5
            std_steps = (sum([(s - avg_steps) ** 2 for s in steps_list]) / runs) ** 0.5
            results.append({
                'Size': size,
                'Algorithm': algorithm,
                'Success Rate (%)': success_rate,
                'Avg Time (s)': avg_time,
                'Std Time (s)': std_time,
                'Avg Steps': avg_steps,
                'Std Steps': std_steps
            })

    # Guardar todos los resultados en un archivo CSV
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Size', 'Algorithm', 'Success Rate (%)', 'Avg Time (s)', 'Std Time (s)', 'Avg Steps', 'Std Steps']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

    # Generar gráficos de tiempo y pasos
    plot.whiskers(
        data=[all_time_data[alg] for alg in ['Simulated Annealing', 'Hill Climbing', 'Genetic Algorithm', 'CSP Backtracking', 'CSP Forward Checking']],
        title='Comparación de Tiempo para Todos los Tamaños',
        x_label='Algorithm',
        y_label='Execution Time (s)',
        filename='time_comparison_all_sizes',
        algList=['Simulated Annealing', 'Hill Climbing', 'Genetic Algorithm', 'CSP Backtracking', 'CSP Forward Checking']
    )

    plot.whiskers(
        data=[all_steps_data[alg] for alg in ['Simulated Annealing', 'Hill Climbing', 'Genetic Algorithm', 'CSP Backtracking', 'CSP Forward Checking']],
        title='Comparación de Estados Visitados para Todos los Tamaños',
        x_label='Algorithm',
        y_label='Number of Steps',
        filename='steps_comparison_all_sizes',
        algList=['Simulated Annealing', 'Hill Climbing', 'Genetic Algorithm', 'CSP Backtracking', 'CSP Forward Checking']
    )
    # Calcular y mostrar estadísticas de pasos
    print("\n--- Estadísticas de Estados Previos (Promedio y Desviación Estándar) ---\n")
    for algorithm in ['Simulated Annealing', 'Hill Climbing', 'Genetic Algorithm', 'CSP Backtracking', 'CSP Forward Checking']:
        all_steps = all_steps_data[algorithm] 
        if all_steps:
            avg_steps = sum(all_steps) / len(all_steps)
            std_steps = (sum((s - avg_steps) ** 2 for s in all_steps) / len(all_steps)) ** 0.5
            print(f"{algorithm}:")
            print(f"  Promedio de estados previos (steps): {avg_steps:.2f}")
            print(f"  Desviacion estandar de estados previos (steps): {std_steps:.2f}\n")

    # Calcular y mostrar estadísticas de tiempos de ejecución
    print("\n--- Estadísticas de Tiempos de Ejecución (Promedio y Desviación Estándar) ---\n")
    for algorithm in ['Simulated Annealing', 'Hill Climbing', 'Genetic Algorithm', 'CSP Backtracking', 'CSP Forward Checking']:
        all_times = all_time_data[algorithm]
        if all_times:
            avg_time = sum(all_times) / len(all_times)
            std_time = (sum((t - avg_time) ** 2 for t in all_times) / len(all_times)) ** 0.5
            print(f"{algorithm}:")
            print(f"  Promedio de tiempo de ejecucion: {avg_time:.2f} segundos")
            print(f"  Desviacion estandar de tiempo de ejecucion: {std_time:.2f} segundos\n")


run_experiment()


