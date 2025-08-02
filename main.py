from enum import Enum

import pyxel

from model.world import World
from model.ball import Ball
from model.common import WIDTH, HEIGHT, TITLE, SUBTITLE

class State(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title=TITLE, fps=120)
        pyxel.load("sprites.pyxres")
        pyxel.mouse(True)

        self.world = World(pyxel.tilemap(0))
        self.ball = Ball()
        self.state = State.MENU

        pyxel.run(self.update, self.draw)

    def game_update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.state = State.PLAYING

    def game_render(self):
        self.ball.render()

    def menu_render(self):
        text_width = pyxel.FONT_WIDTH * len(TITLE)
        pyxel.text(WIDTH / 2 - text_width / 2, HEIGHT / 2 - pyxel.FONT_HEIGHT, TITLE, pyxel.COLOR_WHITE)

        text_width = pyxel.FONT_WIDTH * len(SUBTITLE)
        pyxel.text(WIDTH / 2 - text_width / 2, HEIGHT / 2, SUBTITLE, pyxel.COLOR_RED)

    def update(self):
        match self.state:
            case State.MENU:
                self.game_update()
            case State.PLAYING:
                self.ball.update()
            case State.GAME_OVER:
                pass

    def draw(self):
        pyxel.cls(0)
        
        pyxel.bltm(0,0,0,0,0,160,120)

        match self.state:
            case State.MENU:
                self.menu_render()
            case State.PLAYING:
                self.game_render()
            case State.GAME_OVER:
                pass

App()