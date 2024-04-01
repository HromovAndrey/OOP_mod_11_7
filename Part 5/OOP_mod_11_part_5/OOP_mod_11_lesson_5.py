class Animal:
    def sound(self):
        print("Some sound: hrrr")
    def make_noise(self):
        self.sound()
        self.sound()
        self.sound()
        self.sound()

class Dog(Animal):
    def run(self):
        print('dog is running')
    def sound(self):
        print("Hav, hav")

class Cat(Animal):
     def sound(self):
         super().sound()
         print("Miau")
     def get_super(self):
         print(super())
#obj = Dog()
#print(obj.sound())
#print()
#obj.make_noise()


cat = Cat()
cat.sound()


class Figue:
    def __init__(self, area):
        self.area = area
        print('init from Figue')

class Circle(Figue):
    def __init__(self, area, radius, *args):
        super._radius = radius
        print("init from Circle")

    def print_info(self):
        print(f"{self._area=}")
        print(f"{self._radius=")

obj = Circle(20, 3)


class Parent:
    def __init__(self, name, = "Anna"):
        self.name = name
        print("Я батько - ініціалізувався")

class Child(Parent):
    def __init__(self, name, additional_info):
        #super().__init__(name) #Виклик конструктора батківського класу
        self.additional_info = additional_info
        #self.name = name

# Створення обьекта
child_obj = Child("ChildName", "Additionalinfo")
print(child_obj.name)

class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender
class Student(Person):
     def __init__(self,name, age, gender, student_id):
         super().__init__(name, age, gender)
         self._student_id = student_id
     def get_id(self):
         return self._student_id
     def set_id(self, new_id):
         self._student_id = new_id

     def get_info(self, objects):
         print(f"Студент {self._name }")
