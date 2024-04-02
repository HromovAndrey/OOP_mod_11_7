class MyDeskReptory:
    def __get__(self, instance, owner):
        print("Gettint the attribute")
        print(self)
        print(instance)
        print(owner)

    def __set__(self, instance, value):
        print("Setting the attribute")

class MyClass ():
       atr = MyClass

class MyDescriptor:
    def __init__(self, amount):
        print("discriptor get")
        self._amount = amount
    def __get__(self, instance, owner):
        print("discreptor get")
        return self._amount

    def __set__(self, instance, value):
        print("descriptor set ")
        if value >= 0:
            self._amount =

class FinancialData:
     amount = MyDescriptor()
obj = FinancialData()
print(obj.amount)
obj.amount =

decor(1, 2, "asd")
print(type(decor))
calculator = DiscountCalculator()

