import random

class Environment:
    def __init__(self, sizeX, sizeY, init_posX, init_posY, dirt_rate):
        self.sizeX = sizeX  #Filas
        self.sizeY = sizeY  #Columnas
        self.agent_pos = [init_posX, init_posY]
        self.grid = [['' for i_ in range(sizeY)] for _ in range(sizeX)]
        self.performance = 0
        self.dirt_rate = dirt_rate

        # Colocar suciedad según el dirt_rate
        for i in range(sizeX):
            for j in range(sizeY):
                if random.random() < dirt_rate:  #num entre 0 y 1
                    self.grid[i][j] = 'Dirt'  #Si es menor al dirt rate, entonces está sucio

    def accept_action(self, action):
        x, y = self.agent_pos
        if action == 'Up' and x > 0:
            self.agent_pos[0] -= 1  #Nos movemos una fila arriba
        elif action == 'Down' and x < self.sizeX - 1:
            self.agent_pos[0] += 1  #Nos movemos una fila abajo
        elif action == 'Left' and y > 0:
            self.agent_pos[1] -= 1  #Nos movemos una columna, a la derecha
        elif action == 'Right' and y < self.sizeY - 1:
            self.agent_pos[1] += 1  #Nos movemos una columna, a la izquierda
        elif action == 'Clean':
            if self.grid[x][y] == 'Dirt':
                self.grid[x][y] = ' '  # El agente limpia
                self.performance += 1  #Sumamos un punto por limpiar
        elif action == 'Idle':
            pass

    def is_dirty(self):
        x, y = self.agent_pos
        return self.grid[x][y] == 'Dirt'

    def get_performance(self):
        return self.performance

    def print_environment(self):
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                print(self.matrix[i][j], end=' ')
            print( )