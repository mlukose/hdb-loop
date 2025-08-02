import pyxel
import model.common as common

MAX_VELOCITY = 10
FRICTION = 0.95

class Ball:
    def __init__(self):
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
            self.vel_x = -self.vel_x
            self.vel_y = -self.vel_y
        
        future_x = self.x + self.vel_x
        future_y = self.y + self.vel_y
        if future_x < 0 or future_x >= common.WIDTH:
            self.vel_x = -self.vel_x
        if future_y < 0 or future_y >= common.HEIGHT:
            self.vel_y = -self.vel_y

        self.x += self.vel_x
        self.y += self.vel_y

        self.vel_x *= FRICTION
        self.vel_y *= FRICTION

    def render(self):
        pyxel.pset(self.x, self.y, pyxel.COLOR_WHITE)

        if self.is_dragging:
            pyxel.line(self.x, self.y, self.x + (-self.drag_start_x + pyxel.mouse_x), self.y + (-self.drag_start_y
                                                                                       + pyxel.mouse_y), pyxel.COLOR_RED)
