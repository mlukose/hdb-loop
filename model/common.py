import pyxel

WIDTH = 160
HEIGHT = 120

def limit_vector_length(x, y, limit) -> tuple[int, int]:
    length = x * x + y * y

    if length <= limit * limit:
        return (x, y)

    length = pyxel.sqrt(length)

    return ((x / length) * limit, (y / length) * limit)
