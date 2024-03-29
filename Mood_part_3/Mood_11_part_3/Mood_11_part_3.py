#Завдання 1
#До вже реалізованого класу «Дріб» додайте статичний метод, який при виклику повертає кількість створених об’єктів
#класу «Дріб».

class Дріб:
    кількість_створених_обєктів = 0

    def __init__(self, чисельник, знаменник):
        self.чисельник = чисельник
        self.знаменник = знаменник
        Дріб.кількість_створених_обєктів += 1

    @staticmethod
    def кількість_обєктів():
        return Дріб.кількість_створених_обєктів

дріб1 = Дріб(1, 2)
дріб2 = Дріб(3, 4)
дріб3 = Дріб(5, 6)

print("Кількість створених об'єктів класу 'Дріб':", Дріб.кількість_обєктів())
#Завдання 2
#Створіть клас для конвертування температури з Цельсія
#у Фаренгейт, і навпаки. У класі має знаходитися два статичні
#методи: для конвертування з Цельсія у Фаренгейт і для конвертування з Фаренгейта у Цельсій. Також клас має розрахувати
#кількість підрахунків температури та повернути це значення
#статичним методом

class TemperatureConverter:
    підрахунки_температури = 0

    @staticmethod
    def celsius_to_fahrenheit(цельсій):
        TemperatureConverter.підрахунки_температури += 1
        return (цельсій * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(фаренгейт):
        TemperatureConverter.підрахунки_температури += 1
        return (фаренгейт - 32) * 5/9

    @staticmethod
    def кількість_підрахунків_температури():
        return TemperatureConverter.підрахунки_температури

цельсій = 30
фаренгейт = TemperatureConverter.celsius_to_fahrenheit(цельсій)
print(f"{цельсій} градусів Цельсія дорівнює {фаренгейт} градусам Фаренгейта.")

новий_цельсій = TemperatureConverter.fahrenheit_to_celsius(фаренгейт)
print(f"{фаренгейт} градусів Фаренгейта дорівнює {новий_цельсій} градусам Цельсія.")

print("Кількість підрахунків температури:", TemperatureConverter.кількість_підрахунків_температури())
#Завдання 3
#Створіть клас для конвертування з метричної системи в
#англійську, та навпаки. Реалізуйте функціональність у вигляді
#статичних методів. Обов’язково реалізуйте конвертування
#заходів довжини.

class LengthConverter:
    підрахунки_довжини = 0

    @staticmethod
    def meters_to_feet(метри):
        LengthConverter.підрахунки_довжини += 1
        return метри * 3.28084

    @staticmethod
    def feet_to_meters(фути):
        LengthConverter.підрахунки_довжини += 1
        return фути / 3.28084

    @staticmethod
    def кількість_підрахунків_довжини():
        return LengthConverter.підрахунки_довжини

метри = 10
фути = LengthConverter.meters_to_feet(метри)
print(f"{метри} метрів дорівнює {фути} футам.")

нові_метри = LengthConverter.feet_to_meters(фути)
print(f"{фути} футів дорівнює {нові_метри} метрам.")

print("Кількість підрахунків довжини:", LengthConverter.кількість_підрахунків_довжини())
#Завдання 4
# Створіть клас InformationSystem, який має атрибут data
#- словник, де ключі - це імена користувачів, а значення -
#список їх контактів. Реалізуйте методи класу для додавання
#нових користувачів та їх контактів.
class InformationSystem:
    def __init__(self):
        self.data = {}

    def add_user(self, username):
        if username not in self.data:
            self.data[username] = []

    def add_contact(self, username, contact):
        if username in self.data:
            self.data[username].append(contact)
        else:
            print(f"Користувача '{username}' не знайдено.")

system = InformationSystem()

system.add_user("John")
system.add_contact("John", "Mary")
system.add_contact("John", "Peter")

system.add_user("Alice")
system.add_contact("Alice", "Bob")

print(system.data)
