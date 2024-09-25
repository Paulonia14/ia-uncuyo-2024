from board import *
import algorithms
import time
import csv
import random
import plot

def run_experiment(sizes=[4, 8, 10], runs=30, filename='results.csv'):
    results = []
    time_data = {'Simulated Annealing': [], 'Hill Climbing': [], 'Genetic Algorithm': []}
    steps_data = {'Simulated Annealing': [], 'Hill Climbing': [], 'Genetic Algorithm': []}
    success_data = {'Simulated Annealing': [], 'Hill Climbing': [], 'Genetic Algorithm': []}
    h_history_data = {'Simulated Annealing': [], 'Hill Climbing': []}
    all_time_data = {'Simulated Annealing': [], 'Hill Climbing': [], 'Genetic Algorithm': []}
    all_steps_data = {'Simulated Annealing': [], 'Hill Climbing': [], 'Genetic Algorithm': []}

    for size in sizes:
        for algorithm in ['Simulated Annealing', 'Hill Climbing', 'Genetic Algorithm']:
            successes = 0
            times = []
            steps_list = []
            h_histories = []
            for _ in range(runs):
                board, queens = generate_board(size)
                start_time = time.time()

                if algorithm == 'Simulated Annealing':
                    solution_found, steps, final_temp, h_history = algorithms.simulated_annealing(board, size, queens)
                    h_histories.append(h_history)
                elif algorithm == 'Hill Climbing':
                    solution_found, steps, h_history = algorithms.hill_climbing(board, size, queens)
                    h_histories.append(h_history)
                else:
                    solution_found, steps, generations = algorithms.genetic_algorithm(queens, size)

                exec_time = time.time() - start_time
                if solution_found:
                    successes += 1
                times.append(exec_time)
                steps_list.append(steps)

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

            # Guardar datos para las gráficas
            time_data[algorithm].append(times)
            steps_data[algorithm].append(steps_list)
            success_data[algorithm].append(success_rate)
            all_time_data[algorithm].extend(times)
            all_steps_data[algorithm].extend(steps_list)
            if algorithm != 'Genetic Algorithm':
                h_history_data[algorithm].append(h_histories)

    # Gráficos de tiempos y pasos para todos los tamaños combinados
    plot.whiskers(
        data=[all_time_data[alg] for alg in ['Simulated Annealing', 'Hill Climbing', 'Genetic Algorithm']],
        title='Comparación de Tiempo para Todos los Tamaños',
        x_label='Algorithm',
        y_label='Execution Time (s)',
        filename='time_comparison_all_sizes',
        algList=['Simulated Annealing', 'Hill Climbing', 'Genetic Algorithm']
    )

    plot.whiskers(
        data=[all_steps_data[alg] for alg in ['Simulated Annealing', 'Hill Climbing', 'Genetic Algorithm']],
        title='Comparación de Estados Visitados para Todos los Tamaños',
        x_label='Algorithm',
        y_label='Number of Steps',
        filename='steps_comparison_all_sizes',
        algList=['Simulated Annealing', 'Hill Climbing', 'Genetic Algorithm']
    )

    # Agregar gráficos de la función H
    for algorithm in ['Simulated Annealing', 'Hill Climbing']:
        for i, size in enumerate(sizes):
            # Asumiendo que quieres el promedio de las ejecuciones
            num_runs = len(h_history_data[algorithm][i])
            max_length = max(len(run_hh) for run_hh in
                             h_history_data[algorithm][i])  # Máximo número de iteraciones en cualquier ejecución
            avg_h_history = [sum(run_hh[j] for run_hh in h_history_data[algorithm][i] if j < len(run_hh)) / num_runs for
                             j in range(max_length)]

            plot.plotData2(avg_h_history, f"{algorithm.lower()}_h_function_{size}", range(1, max_length + 1),
                           f"H Function Over Iterations for {algorithm} (Size {size})", "Iteration", "H Value", 10, 5)


run_experiment()
