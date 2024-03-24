#Завдання 1
#До вже реалізованого класу «Людина» додайте конструктор та необхідні перевантажені методи.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __ne__(self, other):
        return not self.__eq__(other)

person1 = Person("Василь", 30)
person2 = Person("Василь", 30)

print(person1)
print(person1 == person2)
print(person1 != person2)

#Завдання 2
#До вже реалізованого класу «Місто» додайте конструктор та необхідні перевантажені методи.

class City:
    def __init__(self, name, population, country):
        self.name = name
        self.population = population
        self.country = country

    def __str__(self):
        return f"Місто: {self.name}, Населення: {self.population}, Країна: {self.country}"

    def __eq__(self, other):
        return self.name == other.name and self.population == other.population and self.country == other.country

    def __ne__(self, other):
        return not self.__eq__(other)

city1 = City("Київ", 3000000, "Україна")
city2 = City("Київ", 3000000, "Україна")

print(city1)
print(city1 == city2)
print(city1 != city2)

#Завдання 3
#До вже реалізованого класу «Країна» додайте конструктор та необхідні перевантажені методи.

class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __str__(self):
        return f"Країна: {self.name}, Населення: {self.population}, Площа: {self.area}"

    def __eq__(self, other):
        return self.name == other.name and self.population == other.population and self.area == other.area

    def __ne__(self, other):
        return not self.__eq__(other)


country1 = Country("Україна", 40000000, 603700)
country2 = Country("Україна", 40000000, 603700)

print(country1)
print(country1 == country2)
print(country1 != country2)

#Завдання 4
#Реалізуйте клас «Годинник». Збережіть у класі:
#назву моделі годинника, виробника годинника, рік
#випуску, ціну годинника, тип годинника (наручний,
#настінний і т. д.). Реалізуйте конструктор та методи
#класу для введення-виведення даних, а також для
#інших операцій. Використовуйте механізм
#перевантаження методів.

class Clock:
    def __init__(self, model, manufacturer, year, price, clock_type):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.clock_type = clock_type

    def display_info(self):
        print(f"Модель: {self.model}, Виробник: {self.manufacturer}, Рік випуску: {self.year}, "
              f"Ціна: {self.price}, Тип: {self.clock_type}")

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price

clock1 = Clock("G-Shock", "Casio", 2022, 150, "наручний")
clock2 = Clock("Rolex Submariner", "Rolex", 2020, 10000, "наручний")

clock1.display_info()
clock2.display_info()

if clock1 < clock2:
    print("Годинник 1 дешевший за годинник 2")
elif clock1 == clock2:
    print("Годинники мають однакову ціну")
else:
    print("Годинник 2 дешевший за годинник 1")

#Завдання 5
#Реалізуйте клас «Вебсайт». Збережіть у класі: назву
#вебсайту, адресу та опис вебсайту. Реалізуйте конструктор
#та методи класу для введення-виведення даних, а також
#для інших операцій. Використовуйте механізм перевантаження методів.
class Website:
    def __init__(self, name, url, description):
        self.name = name
        self.url = url
        self.description = description

    def display_info(self):
        print(f"Назва: {self.name}, Адреса: {self.url}, Опис: {self.description}")

    def __eq__(self, other):
        return self.name == other.name

website1 = Website("Google", "https://www.google.com", "Пошукова система та інші сервіси")
website2 = Website("Facebook", "https://www.facebook.com", "Соціальна мережа")

website1.display_info()
website2.display_info()

if website1 == website2:
    print("Це однакові вебсайти")
else:
    print("Це різні вебсайти")


