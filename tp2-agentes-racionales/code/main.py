from environment import *
from agent import *
from agent_random import *
import csv
import copy

# tamaños de entornos y dirt rates
sizes = [(2, 2), (4, 4), (8, 8), (16, 16), (32, 32), (64, 64), (128, 128)]
dirt_rates = [0.1, 0.2, 0.4, 0.8]
iterations = 10

results = []


def run_simulation(sizeX, sizeY, dirt_rate):
    init_posX = random.randint(0, sizeX - 1)
    init_posY = random.randint(0, sizeY - 1)

    original_env = Environment(sizeX, sizeY, init_posX, init_posY, dirt_rate)
    agent1 = Agent(copy.deepcopy(original_env))
    agent2 = AgentRandom(copy.deepcopy(original_env))

    initialA1_lives = agent1.lives
    initialA2_lives = agent2.lives

    # Simulación para Agent
    while agent1.lives > 0 and agent1.env.dirt_left > 0:
        agent1.think()
    performance1 = agent1.env.performance
    lives_spent1 = initialA1_lives - agent1.lives

    # Simulación para AgentRandom
    while agent2.lives > 0 and agent2.env.dirt_left > 0:
        agent2.think()
    performance2 = agent2.env.performance
    lives_spent2 = initialA2_lives - agent2.lives

    return performance1, lives_spent1, performance2, lives_spent2


# Ejecutar simulaciones y guardar resultados
results = []

for size in sizes:
    for dirt_rate in dirt_rates:
        for i in range(iterations):
            performance1, lives_spent1, performance2, lives_spent2 = run_simulation(size[0], size[1], dirt_rate)
            results.append({
                'Size': f'{size[0]}x{size[1]}',
                'Dirt Rate': dirt_rate,
                'Agent_Performance': performance1,
                'Agent_Lives_Spent': lives_spent1,
                'AgentRandom_Performance': performance2,
                'AgentRandom_Lives_Spent': lives_spent2
            })

# Guardar resultados en un archivo CSV
with open('simulation_results.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Size', 'Dirt Rate', 'Agent_Performance', 'Agent_Lives_Spent',
                                              'AgentRandom_Performance', 'AgentRandom_Lives_Spent'])
    writer.writeheader()
    writer.writerows(results)

print("Resultados guardados en 'simulation_results.csv'")