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

class MyClass:
    def __init__(self):
        self.__private_vriable = 10

    def _private_method(self):
        print("Це приватний метод")

obj = MyClass
print(obj._private_variable)
obj._private_method()

class BankAccount:
    def __init__(self, balance):
        self._balance = balance #ініцевузалі обьект
    def get_balance(self):
        return self.__balance
    def  deposite(self, amount):
        self._balance += amount
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
             print("Недостатньо коштів на рахунку")
    def get_balance(self):
        return self._balance
account = BankAccount(1000)
account.deposite(500)
account.withdram(200)
print(account.get_balance())
