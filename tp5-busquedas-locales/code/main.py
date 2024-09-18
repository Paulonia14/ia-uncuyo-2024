from board import *
import algorithms
import time
import csv
import plot
import random

"""
def run_experiment(sizes=[4, 8, 10], runs=30, filename='results.csv'):
    results = []

    for size in sizes:
        for algorithm in ['Simulated Annealing', 'Hill Climbing']:
            successes = 0
            times = []
            steps_list = []
            board, queens = generate_board(size)
            for _ in range(runs):
                start_time = time.time()
                if algorithm == 'Simulated Annealing':
                    solution_found, steps, final_temp = algorithms.simulated_annealing(board, size, queens)
                else:  # Hill Climbing
                    solution_found, steps = algorithms.hill_climbing(board, size, queens)
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
"""
sizes = [4,8,10,12,15]
runs = 30
for size in sizes:
    for algorithm in ['Simulated Annealing', 'Hill Climbing']:
        times_h=[]
        steps_h=[]
        successes_h = 0
        successes_sa = 0
        times_sa=[]
        steps_sa=[]
        board,queens = generate_board(size)
        for _ in range(runs):
            start_time = time.time()
            if algorithm == 'Simulated Annealing':
                solution_found, steps, final_temp = algorithms.simulated_annealing(board, size, queens)
                exec_time = time.time() - start_time
                times_sa.append(exec_time)
                steps_sa.append(steps)
                if solution_found:
                    successes_sa +=1
            else:
                solution_found, steps = algorithms.hill_climbing(board, size, queens)
                exec_time = time.time() - start_time
                times_h.append(exec_time)
                steps_h.append(steps)
                if solution_found:
                    successes_h +=1
        success_rate_h = ( successes_h / runs ) * 100
        success_rate_sa = ( successes_sa / runs ) * 100

            



    # Guardar en un archivo CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Size', 'Algorithm', 'Success Rate (%)', 'Avg Time (s)', 'Std Time (s)', 'Avg Steps', 'Std Steps'])
        writer.writeheader()
        writer.writerows(results)

run_experiment()
plot.plotData()
