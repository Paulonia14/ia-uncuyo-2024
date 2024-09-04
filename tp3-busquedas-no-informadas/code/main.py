import gymnasium as gym
from gymnasium import wrappers
import time
import random
import queue
from agent import *

#from gymnasium.envs.toy_text.frozen_lake import generate_random_map
#env = gym.make('FrozenLake-v1', desc=generate_random_map(size=size, p=(1-0.08), seed=1), render_mode='human')

iterations = 30
size = 10
hole_prob = 0.08
saved_envs = []

def generate_env(size, hole_prob):
    start_posx = random.randint(0, size - 1)
    start_posy = random.randint(0, size - 1)
    goal_posx = random.randint(0, size - 1)
    goal_posy = random.randint(0, size - 1)

    while goal_posx == start_posx and goal_posy == start_posy:  # Que la meta y el estado inicial no sean iguales
        goal_posx = random.randint(0, size - 1)
        goal_posy = random.randint(0, size - 1)

    desc = []
    for i in range(size):
        fila = ""
        for j in range(size):
            if start_posx == i and start_posy == j:
                fila += 'S'  # Estado inicial
            elif goal_posx == i and goal_posy == j:
                fila += 'G'  # Meta
            else:
                if random.random() < hole_prob:
                    fila += 'H'  # Agujero
                else:
                    fila += 'F'  # Hielo
        desc.append(fila)
    return desc, (start_posx, start_posy), (goal_posx, goal_posy)

for i in range(2):
    for j in range(iterations):
        desc, (start_posx, start_posy), (goal_posx, goal_posy) = generate_env(size, hole_prob)
        saved_envs.append(desc)  # Entornos
        env = gym.make('FrozenLake-v1', desc=desc, is_slippery=False, render_mode='human')

        # Vidas
        lives = 1000
        env = wrappers.TimeLimit(env, lives)

        # print("Número de estados:", env.observation_space.n)
        # print("Número de acciones:", env.action_space.n)

        # Configurar el agente
        scenario = i+1
        agent = Agent(env, scenario)

        initial_state = agent.position_to_state((start_posx, start_posy), size)
        goal_state = agent.position_to_state((goal_posx, goal_posy), size)

        # Búsqueda por Anchura
        env.reset()
        path = agent.bfs(initial_state, goal_state, size, desc)
        agent.execute_path(path)

        # Búsqueda por Profundidad
        env.reset()
        path = []
        path = agent.dfs(initial_state, goal_state, size, desc)
        agent.execute_path(path)

        # Búsqueda por Profundidad Limitada (10)
        env.reset()
        path = []
        path = agent.limitedSearch(initial_state, goal_state, size, desc)
        agent.execute_path(path)

        # Búsqueda de Costo Uniforme
        env.reset()
        path = []
        path = agent.uniformCost_search(initial_state, goal_state, size, desc)
        agent.execute_path(path)





# Guardar entornos
with open('entornos_guardados.txt', 'w') as file:
    for desc in saved_envs:
        for row in desc:
            file.write(row + "\n")
        file.write("\n")






