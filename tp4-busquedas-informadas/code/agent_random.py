import random

class RandomAgent:
    ACTIONS = {
        0: (0, -1),  # izq
        1: (1, 0),   # Abajo
        2: (0, 1),  # derecha
        3: (-1, 0)    # arriba
    }

    def __init__(self, env):
        self.env = env

    def get_action_cost(self, action, scenario): # Saca los costos segun el escenario
        if scenario == 1:
            return 1
        elif scenario == 2:
            return action + 1

    def state_to_position(self, state, size):
        # Convierte un estado a una posicion (fila, columna)
        return (state // size, state % size)

    def position_to_state(self, pos, size):
        # Convierte una posicion (fila, columna) a un estado
        return pos[0] * size + pos[1]

    def is_valid_position(self, pos, size): # Si la pos está dentro de los limites
        x, y = pos
        return 0 <= x < size and 0 <= y < size

    # Crear camino
    def search_path_random(self, initial_state, goal_state, size, desc):
        states = 0
        path = []
        lives = 1000
        current_state = initial_state
        current_pos = self.state_to_position(current_state, size)
        while current_state != goal_state and lives > 0:
            next_action = random.randint(0, len(self.ACTIONS) - 1)
            aux = self.ACTIONS[next_action]
            x, y = aux
            next_position = (current_pos[0] + x, current_pos[1] + y)
            posx, posy = next_position
            while not self.is_valid_position(next_position, size) or desc[posx][posy] == 'H':
                next_action = random.randint(0, len(self.ACTIONS) - 1)
                aux = self.ACTIONS[next_action]
                x, y = aux
                next_position = (current_pos[0] + x, current_pos[1] + y)
                posx, posy = next_position
            next_state = self.position_to_state(next_position, size)
            states += 1
            path.append(next_action)
            current_state = next_state
            current_pos = next_position
            #print(f"Acción: {next_action}")
            next_obs, reward, done, truncated, _ = self.env.step(next_action)
            #print(f"Vidas: {lives}")
            lives -= 1
        if done:
            if reward > 0:
                print("El agente ganó!")
            else:
                print("El agente murió.")
        if lives == 0 and current_state != goal_state:
            print(" olaaaaaaaaaaaaaa ")
            return states, None
        return states, path


