import random

class Agent:
    def __init__(self, env):
        self.env = env

    def up(self):
        self.env.accept_action('Up')

    def down(self):
        self.env.accept_action('Down')

    def left(self):
        self.env.accept_action('Left')

    def right(self):
        self.env.accept_action('Right')

    def clean(self):
        self.env.accept_action('Clean')

    def idle(self):
        self.env.accept_action('Idle')

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