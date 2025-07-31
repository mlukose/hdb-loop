class WorldItem:
    #Where in the resource file each is
    GRASS = (3,1)
    FLOOR = (5,1)
    PLAYER = (1,1)

class World:
    #In Tiles where each tile is 16x16
    HEIGHT = 16
    WIDTH = 16

    def __init__(self, tilemap):
        self.tilemap = tilemap