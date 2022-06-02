class Shape:
    def __init__(self):
        self.mohit = 0
        self.world = 0
class Rectangle(Shape):
    def __init__(self, length, breadth):
        Shape.mohit = (length + breadth) * 2
        Shape.world = length * breadth
    def show_mohit(self):
        return Shape.mohit
    def show_world(self):
        return Shape.world
class Circle(Shape):
    def __init__(self, radius):
        Shape.mohit = (radius * 2) * 3.14
        Shape.world = (radius * radius) * 3.14
    def show_mohit(self):
        return Shape.mohit
    def show_world(self):
        return Shape.world
rec = Rectangle(4, 8)
print(f"Mohit Mostatil >> {rec.show_mohit()} world: {rec.show_world()}")
cir = Circle(6 / 3.14)
print(f"Mohit Dayereh >> {cir.show_mohit()} world: {cir.show_world()}")
