
## Super function is used to access variables from it's parent class or sibling classes based on MRO (Method Order Resolution)
###

class attributes:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Cube(attributes):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.height * self.width

class circle:
    def __init__(self, length):
        self.length = length

    def calc_area(self):
        return self.length**2*3.414

class Square(attributes):
    def __init__(self, length, width):
        super().__init__(length, width)
        # self.height = height

    def area(self):
        return self.length * self.width

c = Cube(3,4,5)
s = Square(1,2)
ci = circle(10)
print(f'volume of the cube is {c.volume()}')
print(f'area of the square is {s.area()}')
print(f'area of the circle is {ci.calc_area()}')
# print(s.area())