import pyxel
from model.player import Player
from model.world import World

class App:
    def __init__(self):
        pyxel.init(160, 120, title= "Hello World")
        pyxel.load("sprites.pyxres")

        self.world = World(pyxel.tilemap(0))
        self.player = Player()
        pyxel.run(self.update, self.draw)

        

    def update(self):
        #TODO: Look up how to make the movement properly (IDK what order to do the keys in or whatever)
        if pyxel.btn(pyxel.KEY_A):
            self.player.move_left()
        if pyxel.btn(pyxel.KEY_D):
            self.player.move_right()
        if pyxel.btn(pyxel.KEY_W):
            self.player.move_up()
        if pyxel.btn(pyxel.KEY_S):
            self.player.move_down()


        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.player.x, self.player.y, 
                  self.player.IMG, 
                  self.player.U, self.player.V, 
                  self.player.WIDTH, self.player.HEIGHT)
        
App()
