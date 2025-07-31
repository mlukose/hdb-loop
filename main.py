import pyxel
from model.world import World
from model.ball import Ball
from model.common import WIDTH, HEIGHT

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title= "Loop Ball", fps=60)
        pyxel.load("sprites.pyxres")

        self.world = World(pyxel.tilemap(0))
        self.ball = Ball()

        pyxel.run(self.update, self.draw)

    def update(self):
        self.ball.update()

    def draw(self):
        pyxel.cls(0)

        self.ball.render()
        
App()
