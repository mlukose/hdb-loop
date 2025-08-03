import pyxel

WIDTH = 128
HEIGHT = 128
TITLE = "Loop Golf"
SUBTITLE = "Press space to play"
GAME_OVER_TITLE = "You Win! Score: "
NUM_LEVELS = 3

def limit_vector_length(x, y, limit) -> tuple[int, int]:
    length = x * x + y * y

    if length <= limit * limit:
        return (x, y)

    length = pyxel.sqrt(length)

    return ((x / length) * limit, (y / length) * limit)
