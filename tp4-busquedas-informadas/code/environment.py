from random import randint, random

def generate_env(size, hole_prob):
    start_posx = randint(0, size - 1)
    start_posy = randint(0, size - 1)
    goal_posx = randint(0, size - 1)
    goal_posy = randint(0, size - 1)

    while goal_posx == start_posx and goal_posy == start_posy:  # Que la meta y el estado inicial no sean iguales
        goal_posx = randint(0, size - 1)
        goal_posy = randint(0, size - 1)

    desc = []
    for i in range(size):
        fila = ""
        for j in range(size):
            if start_posx == i and start_posy == j:
                fila += 'S'  # Estado inicial
            elif goal_posx == i and goal_posy == j:
                fila += 'G'  # Meta
            else:
                if random() < hole_prob:
                    fila += 'H'  # Agujero
                else:
                    fila += 'F'  # Hielo
        desc.append(fila)
    return desc, (start_posx, start_posy), (goal_posx, goal_posy)