class WorldItem:
    #Where in the resource file each is
    GRASS = (0,0)
    DIRT = (1,0)
    SAND = (2,0)
    BLANK = (3,0)

class World:
    #In Tiles where each tile is 16x16
    HEIGHT = 16
    WIDTH = 16

    def __init__(self, tilemap):
        self.tilemap = tilemap

