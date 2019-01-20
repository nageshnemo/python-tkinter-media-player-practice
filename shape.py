import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print("Area is",math.pi * math.pow(self.radius,2))