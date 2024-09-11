import queue

class Agent:
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

    def is_valid_position(self, pos, size): # Si la pos está dentro de los limites
        x, y = pos
        return 0 <= x < size and 0 <= y < size

    def state_to_position(self, state, size):
        # Convierte un estado a una posicion (fila, columna)
        return (state // size, state % size)

    def position_to_state(self, pos, size):
        # Convierte una posicion (fila, columna) a un estado
        return pos[0] * size + pos[1]


    # ----- Búsquedas -----
    def bfs(self, initial_state, goal_state, size, desc):
        states = 0
        frontier = queue.Queue()
        frontier.put((initial_state, []))
        explored = set()
        while not frontier.empty():
            current_state, path = frontier.get()
            current_pos = self.state_to_position(current_state, size)
            if current_state == goal_state: # Llegó
                return path, states
            if current_state not in explored:
                explored.add(current_state)
                for action, (ax, ay) in self.ACTIONS.items():
                    next_pos = (current_pos[0] + ax, current_pos[1] + ay)
                    if self.is_valid_position(next_pos, size):
                        x, y = next_pos
                        if desc[x][y] != 'H':  # agujero
                            next_state = self.position_to_state(next_pos, size)
                            if next_state not in explored:
                                frontier.put((next_state, path + [action]))
                                states += 1
        print("No se encontró un camino por BFS.")
        return None, states

    def dfs(self, initial_state, goal_state, size, desc):
        states = 0
        stack = [(initial_state, [])] #frontier
        explored = set()
        while stack:
            current_state, path = stack.pop()
            current_pos = self.state_to_position(current_state, size)
            if current_state == goal_state:  # Llegó
                return path, states
            if current_state not in explored:
                explored.add(current_state)
                for action, (ax, ay) in self.ACTIONS.items():
                    next_pos = (current_pos[0] + ax, current_pos[1] + ay)
                    if self.is_valid_position(next_pos, size):
                        x, y = next_pos
                        if desc[x][y] != 'H':  # Agujero
                            next_state = self.position_to_state(next_pos, size)
                            if next_state not in explored:
                                stack.append((next_state, path + [action]))
                                states += 1
        print("No se encontró un camino por DFS.")
        return None, states

    def limitedSearch(self, initial_state, goal_state, size, desc, limit=10): # Limite = 10
        states = 0
        stack = [(initial_state, [], 0)]  # Profundidad (depth) de 0
        explored = set()
        while stack:
            current_state, path, depth = stack.pop()
            current_pos = self.state_to_position(current_state, size)
            if current_state == goal_state: # Llegó
                return path, states
            if depth < limit: # Que la profundidad no pase el límite (10)
                if current_state not in explored:
                    explored.add(current_state)
                    for action, (ax, ay) in self.ACTIONS.items():
                        next_pos = (current_pos[0] + ax, current_pos[1] + ay)
                        if self.is_valid_position(next_pos, size):
                            x, y = next_pos
                            if desc[x][y] != 'H': # Agujero
                                next_state = self.position_to_state(next_pos, size)
                                if next_state not in explored:
                                    stack.append((next_state, path + [action], depth +1)) # Le sumo 1 a la profundidad
                                    states += 1
        print("No se encontró un camino por Búsqueda Limitada.")
        return None, states

    def uniformCost_search(self, initial_state, goal_state, size, desc, scenario):
        states = 0
        frontier = queue.PriorityQueue()
        explored = set()
        frontier.put((0, initial_state, []))
        while not frontier.empty():
            path_cost, current_state, path = frontier.get()
            if current_state == goal_state: # Llegó
                return path, states
            if current_state not in explored:
                explored.add(current_state)
                current_pos = self.state_to_position(current_state, size)
                for action, (ax, ay) in self.ACTIONS.items():
                    next_pos = (current_pos[0] + ax, current_pos[1] + ay)
                    if self.is_valid_position(next_pos, size):
                        x, y = next_pos
                        if desc[x][y] != 'H': # Agujero
                            next_state = self.position_to_state(next_pos, size)
                            step_cost = self.get_action_cost(action, scenario)
                            new_path_cost = path_cost + step_cost
                            if next_state not in explored:
                                frontier.put((new_path_cost, next_state, path + [action]))
                                states += 1
                            else: # Reemplaza si el costo es menor al que estaba antes
                                for index, (f_cost, f_state, f_path) in enumerate(frontier.queue): #Enumera la queue tal que [(index, (costo hasta ese estado, estado, camino)), ...]
                                    if f_state == next_state and new_path_cost < f_cost:
                                        frontier.queue[index] = (new_path_cost, next_state, path + [action])
                                        break
        print("No se encontró un camino por Costo Uniforme.")
        return None, states


    def execute_path(self, path):
        # Ejecuta el camino encontrado en el entorno.
        #self.env.render()
        if path:
            for action in path:
                #print(f"Ejecutando acción: {action}")
                next_state, reward, done, truncated, _ = self.env.step(action)
                #print(f"Nuevo estado: {next_state}, Recompensa: {reward}")

                if done:
                    print("El agente ha alcanzado el objetivo.")
                    break
        else:
            print("No se encontró un camino.")

