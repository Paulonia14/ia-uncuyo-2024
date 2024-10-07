import gymnasium as gym
from gymnasium import wrappers
import time
from random import seed
from agent import *
from agent_random import RandomAgent
from environment import *
import csv

#from gymnasium.envs.toy_text.frozen_lake import generate_random_map
#env = gym.make('FrozenLake-v1', desc=generate_random_map(size=size, p=(1-0.08), seed=1), render_mode='human')

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


with open('no-informada-results.csv', mode='w', newline='') as file:

    headers = ['algorithm_name', 'env_n', 'states_n', 'cost_e1', 'cost_e2', 'time', 'solution_found']

    writer = csv.DictWriter(file, fieldnames=headers)

    writer.writeheader()

    for j in range(iterations):
        desc, (start_posx, start_posy), (goal_posx, goal_posy) = generate_env(size, hole_prob)
        env = gym.make('FrozenLake-v1', desc=desc, is_slippery=False, render_mode=None)

        # Vidas (NO funca)
        # lives = 1000
        # env = wrappers.TimeLimit(env, lives)

        # print("Número de estados:", env.observation_space.n)
        # print("Número de acciones:", env.action_space.n)

        # Configurar el agente
        agent = Agent(env)

        initial_state = agent.position_to_state((start_posx, start_posy), size)
        goal_state = agent.position_to_state((goal_posx, goal_posy), size)

        # ---- Búsqueda por Anchura (BFS) ----

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
        # Escenario 1
        cost_e1 = get_cost(agent, path, scenario=1)
        # Escenario 2
        cost_e2 = get_cost(agent, path, scenario=2)

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

        # ---- Búsqueda por Profundidad (DFS) ----

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
        # Escenario 1
        cost_e1 = get_cost(agent, path, scenario=1)
        # Escenario 2
        cost_e2 = get_cost(agent, path, scenario=2)

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

        # ---- Búsqueda por Profundidad Limitada (DLS) ----

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
        # Escenario 1
        cost_e1 = get_cost(agent, path, scenario=1)
        # Escenario 2
        cost_e2 = get_cost(agent, path, scenario=2)

        row = {
            'algorithm_name': 'DLS',
            'env_n': j + 1,
            'states_n': states,
            'cost_e1': cost_e1,
            'cost_e2': cost_e2,
            'time': elapsed_time,
            'solution_found': solution_found
        }
        print("DLS:", row)
        writer.writerow(row)

        # ---- Búsqueda de Costo Uniforme (UCS) ----
        env.reset()
        start_time = time.time()
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
        # Escenario 1
        cost_e1 = get_cost(agent, path, scenario=1)
        # Escenario 2
        cost_e2 = get_cost(agent, path, scenario=2)

        row = {
            'algorithm_name': 'UCS',
            'env_n': j + 1,
            'states_n': states,
            'cost_e1': cost_e1,
            'cost_e2': cost_e2,
            'time': elapsed_time,
            'solution_found': solution_found
        }
        print("UCS:", row)
        writer.writerow(row)

        # ---- Agente random ----
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




