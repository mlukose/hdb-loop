import pyxel
from model import world
import model.common as common
from model.world import World

MAX_VELOCITY = 10
POWER = 0.2
FRICTION = 0.99

WIN_ZONE_X = round(common.WIDTH / 2)
WIN_ZONE_Y = 96

class Ball:
    def __init__(self):
        self.reset()
        self.score = 0

    def reset(self):
        self.x = WIN_ZONE_X
        self.y = WIN_ZONE_Y
        self.vel_x = 0
        self.vel_y = 0
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.is_dragging = False
        self.taken_shot = False
        self.should_advance_level = False

    def update(self, world: World):
         # Detect mouse button press (start of drag)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and not self.taken_shot:
            self.drag_start_x = pyxel.mouse_x
            self.drag_start_y = pyxel.mouse_y
            self.is_dragging = True

        # Detect mouse button release (end of drag)
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and not self.taken_shot:
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
        kill_tiles = [(4,0)]
        # X Collision
        tile_x = round(future_x) // 8
        tile_y = round(self.y) // 8
        tile_idx = world.tilemap.pget(tile_x, tile_y)
        if tile_idx in solid_tiles:
            self.vel_x = -self.vel_x
            pyxel.play(3, 63)
        elif tile_idx in kill_tiles:
            self.reset()
            pyxel.play(3, 0)
            self.score += 1

        # Y Collision
        tile_x = round(self.x) // 8
        tile_y = round(future_y) // 8
        tile_idx = world.tilemap.pget(tile_x, tile_y)
        if tile_idx in solid_tiles:
            self.vel_y = -self.vel_y
            pyxel.play(3, 63)
        elif tile_idx in kill_tiles:
            self.reset()
            pyxel.play(3, 0)
            self.score += 1

        self.x += self.vel_x
        self.y += self.vel_y

        if self.in_win_zone():
            if self.taken_shot:
                self.reset()
                self.score += 1
                self.should_advance_level = True
                pyxel.play(0, 1)
        elif not self.taken_shot:
            self.taken_shot = True

        self.vel_x *= FRICTION
        self.vel_y *= FRICTION

    def render(self):
        for yi in range(5):
            for xi in range(5):
                pyxel.pset(WIN_ZONE_X - 2 + xi, WIN_ZONE_Y - 2 + yi, pyxel.COLOR_GRAY)

        pyxel.pset(WIN_ZONE_X, WIN_ZONE_Y, pyxel.COLOR_BLACK)

        pyxel.pset(self.x, self.y, pyxel.COLOR_WHITE)

        if self.is_dragging:
            dx = -self.drag_start_x + pyxel.mouse_x
            dy = -self.drag_start_y + pyxel.mouse_y

            length = (dx ** 2 + dy ** 2) ** 0.5
            max_length = 40

            if length > max_length:
                scale = max_length / length
                dx *= scale
                dy *= scale

            pyxel.line(
                self.x, self.y, self.x + dx, self.y + dy, pyxel.COLOR_RED
            )
            
    def in_win_zone(self):
        x = round(self.x)
        y = round(self.y)

        return abs(x - WIN_ZONE_X) <= 2 and abs(y - WIN_ZONE_Y) <= 2

    def get_speed_squared(self):
        return self.vel_x ** 2 + self.vel_y ** 2

