import pyxel
import model.common as common

MAX_VELOCITY = 10
POWER = 0.2
FRICTION = 0.98

class Ball:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = common.WIDTH / 2
        self.y = common.HEIGHT / 2
        self.vel_x = 0
        self.vel_y = 0
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.is_dragging = False

    def update(self):
         # Detect mouse button press (start of drag)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.drag_start_x = pyxel.mouse_x
            self.drag_start_y = pyxel.mouse_y
            self.is_dragging = True

        # Detect mouse button release (end of drag)
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            self.drag_end_x = pyxel.mouse_x
            self.drag_end_y = pyxel.mouse_y
            self.is_dragging = False

            self.vel_x = self.drag_end_x - self.drag_start_x
            self.vel_y = self.drag_end_y - self.drag_start_y
            (self.vel_x, self.vel_y) = common.limit_vector_length(self.vel_x, self.vel_y, MAX_VELOCITY)
            self.vel_x = -self.vel_x * POWER
            self.vel_y = -self.vel_y * POWER
        
        future_x = self.x + self.vel_x
        future_y = self.y + self.vel_y

        if future_x <= 0:
            self.x = common.WIDTH
        if future_x >= common.WIDTH:
            self.x = 0
        if future_y <= 0:
            self.y = common.HEIGHT
        if future_y >= common.HEIGHT:
            self.y = 0

        future_x = self.x + self.vel_x
        future_y = self.y + self.vel_y

        #Tilemap collision detection
        solid_tiles = [(1,0), (2,0)] # Index in the tilemap
        # X Collision
        tile_x = round(future_x) // 8
        tile_y = round(self.y) // 8
        tile_idx = pyxel.tilemap(0).pget(tile_x, tile_y)
        if tile_idx in solid_tiles:
            self.vel_x = -self.vel_x

        tile_x = round(self.x) // 8
        tile_y = round(future_y) // 8
        tile_idx = pyxel.tilemap(0).pget(tile_x, tile_y)
        if tile_idx in solid_tiles:
            self.vel_y = -self.vel_y

        self.x += self.vel_x
        self.y += self.vel_y

        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            self.x += 1

        self.vel_x *= FRICTION
        self.vel_y *= FRICTION

    def render(self):
        pyxel.pset(self.x, self.y, pyxel.COLOR_WHITE)

        if self.is_dragging:
            pyxel.line(self.x, self.y, self.x + (-self.drag_start_x + pyxel.mouse_x), self.y + (-self.drag_start_y
                                                                                       + pyxel.mouse_y), pyxel.COLOR_RED)
