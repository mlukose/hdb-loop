import pyxel
import model.common as common

class Ball:
    x = 0
    y = 0

    def __init__(self):
        self.x = common.WIDTH / 2
        self.y = common.HEIGHT / 2

    def update(self):
        pass

    def render(self):
        pyxel.pset(self.x, self.y, pyxel.COLOR_WHITE)
