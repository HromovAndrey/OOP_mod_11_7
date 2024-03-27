class MyClass:
    def public_method(self):
        print("Це публічний  метод")
    def public_method2(self):
        print("Hello from method")
        self.public_method1()

obj = MyClass
obj.public_method()


class MyClass:
    def __init__(self):
        self.protected_attribute = 10

    def _protected_method(self):
        print("Це захищенний метод")

class SubClass(MyClass):
    def access_protected(self):
        print(self._protected_attribute)
        self._protected_method()

obj = SubClass()
obj.access_protected()

class MyClass:
    def __init__(self):
        self.attribute = 20 # PUBLIC
        self._attribute = 10 # private


    def get_attribute(self):
      return self._attribute

obj = MyClass()

print(f"{obj._attribute=}")
print(f"{obj.get_attribute()=}")


class MyClass:
    def __init__(self):
        self.__private_attribute = 20
    def __private_method(self):
       print("Це праватний метод")

obj = MyClass()
#Спробуйте звернутися до приватного атрибуту чи методу викличте AttributeError
print(obj.__private_attribute)
obj.__private_method()

class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Гвидо")

