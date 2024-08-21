import random

class Agent:
    def __init__(self, env, lives=1000):
        self.env = env
        self.lives = lives  #Vidas del agente (empieza con 1000)

    def up(self):
        self.env.accept_action('Up')
        self.lives -= 1  #Cada acción resta una vida

    def down(self):
        self.env.accept_action('Down')
        self.lives -= 1 

    def left(self):
        self.env.accept_action('Left')
        self.lives -= 1 

    def right(self):
        self.env.accept_action('Right')
        self.lives -= 1 

    def clean(self):
        self.env.accept_action('Clean')
        self.lives -= 1 

    def idle(self):
        self.env.accept_action('Idle')
        self.lives -= 1 

    def perspective(self):
        return self.env.is_dirty() #Si es que la pos está sucia

    def think(self):
        if self.perspective():
            self.clean()
        else:
            # Si no hay suciedad en la pos actual, se mueve aleatoriamente
            action = random.choice(['up', 'down', 'left', 'right', 'idle'])
            if action == 'up':
                self.up()
            elif action == 'down':
                self.down()
            elif action == 'left':
                self.left()
            elif action == 'right':
                self.right()
            elif action == 'idle':
                self.idle()
