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


# def sprite_collision(x,y,x2,y2):
#     tile_size = 8
#     if x + tile_size <= x2 or x2 + tile_size <= x:
#         return False
#     if y + tile_size <= y2 or y2 + tile_size <= y:
#         return False
    
#     return True
