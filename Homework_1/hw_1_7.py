class Circle():
    def __init__ (self,r):
        self.radius = r

    def area (self):
        return self.radius**2*3.14

    def perimeter (self):
        return 2*self.radius*3.14

TestCircle = Circle(8)
print(TestCircle.area())
print(TestCircle.perimeter())
