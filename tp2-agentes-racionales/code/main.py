from environment import *
from agent import *
import csv
import random

sizes = [(2, 2), (4, 4), (8, 8), (16, 16), (32, 32), (64, 64), (128, 128)]
dirt_rates = [0.1, 0.2, 0.4, 0.8]
iterations = 10
results = []

def run_simulation(sizeX, sizeY, dirt_rate, steps=1000):  #Genera posiciones aleatorias para el agente
    init_posX = random.randint(0, sizeX - 1)
    init_posY = random.randint(0, sizeY - 1)
    env = Environment(sizeX, sizeY, init_posX, init_posY, dirt_rate)
    agent = Agent(env)
    for _ in range(steps):
        agent.think()
    return env.performance

#Ejecutar la simulación
for size in sizes:
    for dirt_rate in dirt_rates:
        for _ in range(iterations):
            performance = run_simulation(size[0], size[1], dirt_rate)
            results.append([f'{size[0]}x{size[1]}', dirt_rate, performance])

#Escribir los resultados a un archivo CSV
with open('simulation_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Dirt Rate', 'Performance'])
    writer.writerows(results)

print("Resultados guardados en 'simulation_results.csv'")