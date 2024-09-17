class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimetr(self):
        return 2 * (self.width + self.height)

    def is_squre(self):
        return self.width == self.height

    def resize(self):