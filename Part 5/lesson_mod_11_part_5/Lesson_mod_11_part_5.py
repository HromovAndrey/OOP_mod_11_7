class Animal:
    def sound(self):
        print("Some  sound: hrr")
    def make_noise(self):
        self.sound()
        self.sound()
        self.sound()

class Dog(Animal):
    def run(self):
        print("Dog is running")

    def sound(self):
        print("Hav, hav")


class Cat(Animal):
    def sound(self):
        print("Miau")
    def get_super(self):
        super().sound
        print(super())

class MyMode(nn.Module):
    def train(self, data):
#obj = Dog()
print(obj.sound)
print()
obj.make_noise()

cat = Cat()
cat.sound()

class Figure:
    def __init__(self):
        self.area = area
        print(self, area)
class Circle(Figure):
    def __int__(self, area, radius):
        super.radius = radius
        self



