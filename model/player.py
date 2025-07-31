class Player:
    IMG = 0
    U = 0
    V = 0
    WIDTH = 16
    HEIGHT = 16
    DX = 0.5
    DY = 0.5

    def __init__(self):
        self.x = 80
        self.y= 60


    def move_left(self):
        self.x -= self.DX

    def move_right(self):
        self.x += self.DX

    def move_up(self):
        self.y -= self.DY

    def move_down(self):
        self.y += self.DY