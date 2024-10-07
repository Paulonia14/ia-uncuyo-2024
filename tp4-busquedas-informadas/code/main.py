import gymnasium as gym
from gymnasium import wrappers
import time
from random import seed
from agent import *
from agent_random import RandomAgent
from environment import *
import csv
import numpy as np
import matplotlib.pyplot as plt
import os

seed(":D")

iterations = 30
size = 100
hole_prob = 0.08

def get_cost(agent, path, scenario):
    if path is not None and len(path) < 1000:
        if scenario == 1:
            cost = len(path)
        else:
            cost = 0
            for each in path:
                cost = cost + Agent.get_action_cost(agent, each, scenario)
    else:
        cost = 0
    return cost

results = {
    'BFS': {'states': [], 'cost_e1': [], 'cost_e2': [], 'time': []},
    'DFS': {'states': [], 'cost_e1': [], 'cost_e2': [], 'time': []},
    'Limited Search': {'states': [], 'cost_e1': [], 'cost_e2': [], 'time': []},
    'UCS Esc 1': {'states': [], 'cost_e1': [], 'cost_e2': [], 'time': []},
    'UCS Esc 2': {'states': [], 'cost_e1': [], 'cost_e2': [], 'time': []},
    'Agent_Random': {'states': [], 'cost_e1': [], 'cost_e2': [], 'time': []},
    'A* Esc 1': {'states': [], 'cost_e1': [], 'cost_e2': [], 'time': []},
    'A* Esc 2': {'states': [], 'cost_e1': [], 'cost_e2': [], 'time': []}
}

def calculate_and_print_stats():
    for algorithm, data in results.items():
        print(f"Estadísticas para {algorithm}:")
        for key, values in data.items():
            # Filtramos los valores None antes de calcular la media y desviación estándar
            valid_values = [v for v in values if v is not None]
            if valid_values:  # Si hay valores válidos
                mean_val = np.mean(valid_values)
                std_val = np.std(valid_values)
                print(f"{key.capitalize()}: Media = {mean_val}, Desviación estándar = {std_val}")
            else:
                print(f"{key.capitalize()}: No hay datos válidos.")
        print("\n")

# Abrimos el archivo CSV una vez, y lo cerramos después de las iteraciones
file = open('informada-results.csv', mode='w', newline='')
headers = ['algorithm_name', 'env_n', 'states_n', 'cost_e1', 'cost_e2', 'time', 'solution_found']
writer = csv.DictWriter(file, fieldnames=headers)
writer.writeheader()

for j in range(iterations):
    desc, (start_posx, start_posy), (goal_posx, goal_posy) = generate_env(size, hole_prob)
    env = gym.make('FrozenLake-v1', desc=desc, is_slippery=False, render_mode=None)
    agent = Agent(env)
    initial_state = agent.position_to_state((start_posx, start_posy), size)
    goal_state = agent.position_to_state((goal_posx, goal_posy), size)

    # ---- BFS ----
    env.reset()
    start_time = time.time()
    path, states = agent.bfs(initial_state, goal_state, size, desc)
    if path is not None:
        if len(path) > 1000:
            solution_found = False
        else:
            Agent.execute_path(agent, path)
            elapsed_time = time.time() - start_time
            solution_found = True
    else:
        elapsed_time = 0
        solution_found = False
    cost_e1 = get_cost(agent, path, scenario=1)
    cost_e2 = get_cost(agent, path, scenario=2)
    results['BFS']['states'].append(states)
    results['BFS']['cost_e1'].append(cost_e1)
    results['BFS']['cost_e2'].append(cost_e2)
    results['BFS']['time'].append(elapsed_time)

    row = {
        'algorithm_name': 'BFS',
        'env_n': j + 1,
        'states_n': states,
        'cost_e1': cost_e1,
        'cost_e2': cost_e2,
        'time': elapsed_time,
        'solution_found': solution_found
    }
    print("BFS:", row)
    writer.writerow(row)

# ---- DFS ----
    env.reset()
    start_time = time.time()
    path, states = agent.dfs(initial_state, goal_state, size, desc)
    if path is not None:
        if len(path) > 1000:
            solution_found = False
        else:
            Agent.execute_path(agent, path)
            elapsed_time = time.time() - start_time
            solution_found = True
    else:
        elapsed_time = 0
        solution_found = False
    cost_e1 = get_cost(agent, path, scenario=1)
    cost_e2 = get_cost(agent, path, scenario=2)
    results['DFS']['states'].append(states)
    results['DFS']['cost_e1'].append(cost_e1)
    results['DFS']['cost_e2'].append(cost_e2)
    results['DFS']['time'].append(elapsed_time)

    row = {
        'algorithm_name': 'DFS',
        'env_n': j + 1,
        'states_n': states,
        'cost_e1': cost_e1,
        'cost_e2': cost_e2,
        'time': elapsed_time,
        'solution_found': solution_found
    }
    print("DFS:", row)
    writer.writerow(row)

    # ---- Limited Search ----
    env.reset()
    start_time = time.time()
    path, states = agent.limitedSearch(initial_state, goal_state, size, desc, limit=10)
    if path is not None:
        if len(path) > 1000:
            solution_found = False
        else:
            Agent.execute_path(agent, path)
            elapsed_time = time.time() - start_time
            solution_found = True
    else:
        elapsed_time = 0
        solution_found = False
    cost_e1 = get_cost(agent, path, scenario=1)
    cost_e2 = get_cost(agent, path, scenario=2)
    results['Limited Search']['states'].append(states)
    results['Limited Search']['cost_e1'].append(cost_e1)
    results['Limited Search']['cost_e2'].append(cost_e2)
    results['Limited Search']['time'].append(elapsed_time)
                                                
    row = {
        'algorithm_name': 'Limited Search',
        'env_n': j + 1,
        'states_n': states,
        'cost_e1': cost_e1,
        'cost_e2': cost_e2,
        'time': elapsed_time,
        'solution_found': solution_found
    }
    print("Limited Search:", row)
    writer.writerow(row)

    # ---- Uniform Cost Search Esc 1 ----
    env.reset()
    start_time = time.time()
    # escenario 1
    path, states = agent.uniformCost_search(initial_state, goal_state, size, desc, scenario=1)
    if path is not None:
        if len(path) > 1000:
            solution_found = False
        else:
            Agent.execute_path(agent, path)
            elapsed_time = time.time() - start_time
            solution_found = True
    else:
        elapsed_time = 0
        solution_found = False
    cost_e1 = get_cost(agent, path, scenario=1)
    results['UCS Esc 1']['states'].append(states)
    results['UCS Esc 1']['cost_e1'].append(cost_e1)
    results['UCS Esc 1']['cost_e2'].append(None)
    results['UCS Esc 1']['time'].append(elapsed_time)
    row = {
        'algorithm_name': 'UCS Esc 1',
        'env_n': j + 1,
        'states_n': states,
        'cost_e1': cost_e1,
        'cost_e2': None,
        'time': elapsed_time,
        'solution_found': solution_found
    }
    print("UCS:", row)
    writer.writerow(row)
    # ---- Uniform Cost Search Esc 2 ----
    env.reset()
    start_time = time.time()
    # escenario 2
    path, states = agent.uniformCost_search(initial_state, goal_state, size, desc, scenario=2)
    if path is not None:
        if len(path) > 1000:
            solution_found = False
        else:
            Agent.execute_path(agent, path)
            elapsed_time = time.time() - start_time
            solution_found = True
    else:
        elapsed_time = 0
        solution_found = False
    cost_e2 = get_cost(agent, path, scenario=2)
    results['UCS Esc 2']['states'].append(states)
    results['UCS Esc 2']['cost_e1'].append(None)
    results['UCS Esc 2']['cost_e2'].append(cost_e2)
    results['UCS Esc 2']['time'].append(elapsed_time)
    row = {
        'algorithm_name': 'UCS Esc 2',
        'env_n': j + 1,
        'states_n': states,
        'cost_e1': None,
        'cost_e2': cost_e2,
        'time': elapsed_time,
        'solution_found': solution_found
    }
    print("UCS:", row)
    writer.writerow(row)

    # ---- Agente Random ----
    agent_random = RandomAgent(env)
    initial_state = agent_random.position_to_state((start_posx, start_posy), size)
    goal_state = agent_random.position_to_state((goal_posx, goal_posy), size)
    path = []
    env.reset()
    start_time = time.time()
    states, path = agent_random.search_path_random(initial_state, goal_state, size, desc)
    print("Path: ", path)
    elapsed_time = time.time() - start_time
    # Escenario 1
    cost_e1 = get_cost(agent_random, path, scenario=1)
    # Escenario 2
    cost_e2 = get_cost(agent_random, path, scenario=2)
    solution_found = path is not None
    results['Agent_Random']['states'].append(states)
    results['Agent_Random']['cost_e1'].append(cost_e1)
    results['Agent_Random']['cost_e2'].append(cost_e2)
    results['Agent_Random']['time'].append(elapsed_time)

    row = {
        'algorithm_name': 'Agent_Random',
        'env_n': j + 1,
        'states_n': states,
        'cost_e1': cost_e1,
        'cost_e2': cost_e2,
        'time': elapsed_time,
        'solution_found': solution_found
    }
    print("Agent_Random:", row)
    writer.writerow(row)

    # ---- A* Search Esc 1 ----
    env.reset()
    start_time = time.time()
    path, states = agent.a_star(initial_state, goal_state, size, desc,scenario=1)
    if path is not None:
        if len(path) > 1000:
            solution_found = False
        else:
            Agent.execute_path(agent, path)
            elapsed_time = time.time() - start_time
            solution_found = True
    else:
        elapsed_time = 0
        solution_found = False
    cost_e1 = get_cost(agent, path, scenario=1)
    results['A* Esc 1']['states'].append(states)
    results['A* Esc 1']['cost_e1'].append(cost_e1)
    results['A* Esc 1']['cost_e2'].append(None)
    results['A* Esc 1']['time'].append(elapsed_time)

    row = {
        'algorithm_name': 'A* Esc 1',
        'env_n': j + 1,
        'states_n': states,
        'cost_e1': cost_e1,
        'cost_e2': None,
        'time': elapsed_time,
        'solution_found': solution_found
    }
    print("A*:", row)
    writer.writerow(row)

    # ---- A* Search Esc 2 ----
    env.reset()
    start_time = time.time()
    path, states = agent.a_star(initial_state, goal_state, size, desc, scenario=2) 
    if path is not None:
        if len(path) > 1000:
            solution_found = False
        else:
            Agent.execute_path(agent, path)
            elapsed_time = time.time() - start_time
            solution_found = True
    else:
        elapsed_time = 0
        solution_found = False
    cost_e2 = get_cost(agent, path, scenario=2)
    results['A* Esc 2']['states'].append(states)
    results['A* Esc 2']['cost_e1'].append(None)
    results['A* Esc 2']['cost_e2'].append(cost_e2)
    results['A* Esc 2']['time'].append(elapsed_time)

    row = {
        'algorithm_name': 'A* Esc 2',
        'env_n': j + 1,
        'states_n': states,
        'cost_e1': None,
        'cost_e2': cost_e2,
        'time': elapsed_time,
        'solution_found': solution_found
    }
    print("A*:", row)
    writer.writerow(row)

file.close()

# Función para generar gráficos
def plot_statistics(results):
    algorithms = list(results.keys())
    imagesDir = os.path.join(os.path.dirname(__file__), '../images')
    os.makedirs(imagesDir, exist_ok=True)  # Crea la carpeta 'images' si no existe

    # Gráfica de tiempo promedio
    avg_times = [np.mean(results[alg]['time']) if results[alg]['time'] else 0 for alg in algorithms]
    plt.figure(figsize=(10, 5))
    plt.bar(algorithms, avg_times, color='skyblue')
    plt.xlabel('Algoritmo')
    plt.ylabel('Tiempo Promedio (segundos)')
    plt.title('Tiempo promedio por algoritmo')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(imagesDir, 'tiempo_promedio.png'))  # Guardar el gráfico
    plt.clf()  # Limpiar

    # Gráfica de costos del escenario 1
    avg_cost_e1 = [np.mean([x for x in results[alg]['cost_e1'] if x is not None]) if results[alg]['cost_e1'] else 0 for alg in algorithms]
    plt.figure(figsize=(10, 5))
    plt.bar(algorithms, avg_cost_e1, color='lightgreen')
    plt.xlabel('Algoritmo')
    plt.ylabel('Costo Escenario 1')
    plt.title('Costo promedio en Escenario 1 por algoritmo')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(imagesDir, 'costo_esc1.png'))  # Guardar el gráfico
    plt.clf()  # Limpiar

    # Gráfica de costos del escenario 2
    avg_cost_e2 = [np.mean([x for x in results[alg]['cost_e2'] if x is not None]) if results[alg]['cost_e2'] else 0 for alg in algorithms]
    plt.figure(figsize=(10, 5))
    plt.bar(algorithms, avg_cost_e2, color='salmon')
    plt.xlabel('Algoritmo')
    plt.ylabel('Costo Escenario 2')
    plt.title('Costo promedio en Escenario 2 por algoritmo')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(imagesDir, 'costo_esc2.png'))  # Guardar el gráfico
    plt.clf()  # Limpiar

    # Gráfica de estados explorados
    avg_states = [np.mean([x for x in results[alg]['states'] if x is not None]) if results[alg]['states'] else 0 for alg in algorithms]
    plt.figure(figsize=(10, 5))
    plt.bar(algorithms, avg_states, color='orange')
    plt.xlabel('Algoritmo')
    plt.ylabel('Estados Explorados Promedio')
    plt.title('Estados explorados por algoritmo')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(imagesDir, 'estados_explorados.png'))  # Guardar el gráfico
    plt.clf()  # Limpiar

# Al final del código, después de las estadísticas
calculate_and_print_stats()

# Llamamos a la función para generar las gráficas
plot_statistics(results)

