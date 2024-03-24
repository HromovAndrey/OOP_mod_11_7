
class Animals:
    def breath(self):
        print("дихає")

    def move(self):
        print("рухається")

    def eat_food(self):
        print("Їсть")

class Dogs(Animals):
    pass

class Cats(Amimals):
    pass

#Створення екземпляру масиву
my_dogs = Dogs()
my_dogs.breath()