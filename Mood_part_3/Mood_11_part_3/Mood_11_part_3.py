#Завдання 1
#До вже реалізованого класу «Людина» додайте статичний метод, який під час виклику повертає кількість
#створених об’єктів класу «Людина».

class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    @staticmethod
    def get_instance_count():
        return Person.count


person1 = Person("John", 30)
person2 = Person("Alice", 25)

print(Person.get_instance_count())

#Завдання 2
#Створіть клас для підрахунку площі геометричних
#фігур. Клас має надавати функціональність підрахунку
#площі трикутника за різними формулами, площі прямокутника, площі квадрата, площі ромба. Методи класу для
#підрахунку площі реалізуйте за допомогою статичних
#методів. Також клас має розрахувати кількість підрахунків площі та повернути це значення статичним методом.

class AreaCalculator:
    count = 0

    def calculate_triangle_area(base, height):
        AreaCalculator.count += 1
        return 0.5 * base * height

    def calculate_rectangle_area(length, width):
        AreaCalculator.count += 1
        return length * width


    def calculate_square_area(side):
        AreaCalculator.count += 1
        return side ** 2


    def calculate_rhombus_area(diagonal1, diagonal2):
        AreaCalculator.count += 1
        return 0.5 * diagonal1 * diagonal2


    def get_calculation_count():
        return AreaCalculator.count

print("Площа трикутника:", AreaCalculator.calculate_triangle_area(5, 6))
print("Площа прямокутника:", AreaCalculator.calculate_rectangle_area(4, 8))
print("Площа квадрата:", AreaCalculator.calculate_square_area(7))
print("Площа ромба:", AreaCalculator.calculate_rhombus_area(10, 12))

print("Загальна кількість підрахунків:", AreaCalculator.get_calculation_count())


#Завдання 3
#Створіть клас для підрахунку максимуму з чотирьох
#аргументів, мінімуму з чотирьох аргументів, середнє
#арифметичне із чотирьох аргументів, факторіалу аргументу. Реалізуйте функціональність у вигляді статичних
#методів.

class MathOperations:

    def find_maximum(a, b, c, d):
        return max(a, b, c, d)

    def find_minimum(a, b, c, d):
        return min(a, b, c, d)

    def calculate_average(a, b, c, d):
        return (a + b + c + d) / 4

    def calculate_factorial(n):
        if n == 0:
            return 1
        else:
            return n * MathOperations.calculate_factorial(n - 1)

print("Максимум:", MathOperations.find_maximum(5, 10, 3, 8))
print("Мінімум:", MathOperations.find_minimum(5, 10, 3, 8))
print("Середнє арифметичне:", MathOperations.calculate_average(5, 10, 3, 8))
print("Факторіал 5:", MathOperations.calculate_factorial(5))

#Завдання 4
#Створіть клас FileUtils, який має метод класу
#count_lines, який приймає шлях до файлу і повертає
#кількість рядків у файлі.

class FileUtils:

    def count_lines(file_path):
        try:
            with open(file_path, 'r') as file:
                return sum(1 for line in file)
        except FileNotFoundError:
            print("Файл не знайдено.")
            return -1
        except Exception as e:
            print("Виникла помилка:", e)
            return -1

file_path = "example.txt"
line_count = FileUtils.count_lines(file_path)
if line_count != -1:
    print(f"Кількість рядків у файлі {file_path}: {line_count}")

#Завдання 5
#Створіть клас Character, який має атрибути name, health
#та damage. Реалізуйте метод класу attack, який виводить
#повідомлення про атаку гравця.
class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self):
        print(f"{self.name} атакує зі шкодою {self.damage}!")
#Завдання 6
#Створіть клас Student, який має атрибути name, age,
#grade та courses. Реалізуйте метод класу add_course, який
#додає новий предмет до списку курсів студента
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"{course} був доданий до списку курсів студента {self.name}")


