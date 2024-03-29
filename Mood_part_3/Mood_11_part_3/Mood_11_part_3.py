#До вже реалізованого класу «Людина» додайте статичний метод, який під час виклику повертає кількість
#створених об’єктів класу «Людина».
class Human:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Human.count += 1

    @staticmethod
    def get_count():
        return Human.count

human1 = Human("Іван", 25)
human2 = Human("Марія", 30)

print(Human.get_count())


#Завдання 2
#Створіть клас для підрахунку площі геометричних
#фігур. Клас має надавати функціональність підрахунку
#площі трикутника за різними формулами, площі прямокутника, площі квадрата, площі ромба. Методи класу для
#підрахунку площі реалізуйте за допомогою статичних
#mетодів. Також клас має розрахувати кількість підрахунків площі та повернути це значення статичним методом.

class GeometryCalculator:
    calculation_count = 0

    @staticmethod
    def calculate_triangle_area(base, height):
        GeometryCalculator.calculation_count += 1
        return 0.5 * base * height

    @staticmethod
    def calculate_rectangle_area(length, width):
        GeometryCalculator.calculation_count += 1
        return length * width

    @staticmethod
    def calculate_square_area(side):
        GeometryCalculator.calculation_count += 1
        return side ** 2

    @staticmethod
    def calculate_rhombus_area(diagonal1, diagonal2):
        GeometryCalculator.calculation_count += 1
        return 0.5 * diagonal1 * diagonal2

    @staticmethod
    def get_calculation_count():
        return GeometryCalculator.calculation_count

triangle_area = GeometryCalculator.calculate_triangle_area(4, 6)
rectangle_area = GeometryCalculator.calculate_rectangle_area(5, 7)
square_area = GeometryCalculator.calculate_square_area(4)
rhombus_area = GeometryCalculator.calculate_rhombus_area(8, 10)

print("Triangle area:", triangle_area)
print("Rectangle area:", rectangle_area)
print("Square area:", square_area)
print("Rhombus area:", rhombus_area)
print("Total calculations:", GeometryCalculator.get_calculation_count())

#Завдання 3
#Створіть клас для підрахунку максимуму з чотирьох
#аргументів, мінімуму з чотирьох аргументів, середнє
#арифметичне із чотирьох аргументів, факторіалу аргументу. Реалізуйте функціональність у вигляді статичних
#методів.

class MathUtils:
    @staticmethod
    def find_maximum(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def find_minimum(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def calculate_average(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def calculate_factorial(n):
        if n == 0:
            return 1
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

maximum = MathUtils.find_maximum(10, 20, 30, 40)
minimum = MathUtils.find_minimum(10, 20, 30, 40)
average = MathUtils.calculate_average(10, 20, 30, 40)
factorial = MathUtils.calculate_factorial(5)

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)
print("Factorial:", factorial)

#Завдання 4
#Створіть клас FileUtils, який має метод класу
#count_lines, який приймає шлях до файлу і повертає
#кількість рядків у файлі.
class FileUtils:
    @staticmethod
    def count_lines(file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                return len(lines)
        except FileNotFoundError:
            print("File not found.")
            return -1
        except Exception as e:
            print("An error occurred:", str(e))
            return -1

file_path = "example.txt"
lines_count = FileUtils.count_lines(file_path)
if lines_count != -1:
    print("Number of lines in the file:", lines_count)

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
        print(f"{self.name} attacks with {self.damage} damage!")

player1 = Character("Player 1", 100, 20)
player1.attack()

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

student1 = Student("John", 18, 12)
student1.add_course("Math")
student1.add_course("Physics")

print(f"{student1.name} is taking the following courses: {', '.join(student1.courses)}")
