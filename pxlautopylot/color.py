class Color:

    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def is_darker_than(self, color: 'Color') -> bool:
        return self.r < color.r and self.g < color.g and self.b < color.b

    def equals(self, color: 'Color') -> bool:
        return self.r == color.r and self.g == color.g and self.b == color.b

    def __str__(self):
        return "{{ 'r': {0}, 'g': {1}, 'b': {2} }}".format(self.r, self.g, self.b)
