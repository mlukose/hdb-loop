from enum import Enum

import pyxel

from model.world import World
from model.ball import Ball
from model.common import WIDTH, HEIGHT, TITLE, SUBTITLE, NUM_LEVELS

class State(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title=TITLE, fps=120)
        pyxel.load("sprites.pyxres")
        pyxel.mouse(True)
        pyxel.playm(0, loop=True)

        self.reset()
        self.state = State.MENU

        pyxel.run(self.update, self.draw)

    def reset(self):
        self.level = 0
        self.world = World(pyxel.tilemaps[self.level])
        self.ball = Ball()
        self.score = 0

    def game_update(self):
        if self.ball.get_speed_squared() <= 0.000001 and self.ball.taken_shot:
            self.ball.reset()
            self.score += 1

        self.ball.update(self.world)

        if self.ball.should_advance_level:
            self.ball.should_advance_level = False
            self.level += 1
            if self.level >= NUM_LEVELS:
                self.state = State.GAME_OVER
                return
            self.world = World(pyxel.tilemaps[self.level])

    def game_render(self):
        pyxel.bltm(0,0,self.level,0,0,128,128)

        self.ball.render()

        pyxel.text(0, 0, "Score: " + str(self.score), pyxel.COLOR_GRAY)

    def menu_update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.state = State.PLAYING


    def menu_render(self):
        text_width = pyxel.FONT_WIDTH * len(TITLE)
        pyxel.text(WIDTH / 2 - text_width / 2, HEIGHT / 2 - pyxel.FONT_HEIGHT, TITLE, pyxel.COLOR_WHITE)

        text_width = pyxel.FONT_WIDTH * len(SUBTITLE)
        pyxel.text(WIDTH / 2 - text_width / 2, HEIGHT / 2, SUBTITLE, pyxel.COLOR_RED)

    def game_over_update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.reset()
            self.state = State.PLAYING


    def game_over_render(self):
        pyxel.text(WIDTH / 2, HEIGHT / 2, "GAME OVER", pyxel.COLOR_DARK_BLUE)

    def update(self):
        match self.state:
            case State.MENU:
                self.menu_update()
            case State.PLAYING:
                self.game_update()
            case State.GAME_OVER:
                self.game_over_update()

    def draw(self):
        pyxel.cls(0)
        
        match self.state:
            case State.MENU:
                self.menu_render()
            case State.PLAYING:
                self.game_render()
            case State.GAME_OVER:
                self.game_over_render()

App()
