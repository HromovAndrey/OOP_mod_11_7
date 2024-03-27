#Завдання 1
#Створіть клас "Користувач" з атрибутами "ім'я", "вік" та
#"email". Застосуйте інкапсуляцію, щоб забезпечити, що ці
#дані можна отримати лише через методи класу.

class User:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_email(self, email):
        self.__email = email


user1 = User( "Іван", 25, "ivan@example.com")

print("Ім'я користувача:", user1.get_name())
print("Вік користувача:", user1.get_age())
print("Email користувача:", user1.get_email())

#Завдання 2
#Реалізуйте клас "Кошик для покупок" з можливістю
#додавання товарів та підрахунку загальної вартості.
#Застосуйте інкапсуляцію для забезпечення правильності
#обробки даних.

class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_item(self, item_name, quantity, price_per_unit):
        if not isinstance(quantity, int) or not isinstance(price_per_unit, (int, float)):
            print("Помилка: кількість має бути цілим числом, а ціна - числом.")
            return
        if item_name in self.__items:
            self.__items[item_name]['quantity'] += quantity
        else:
            self.__items[item_name] = {'quantity': quantity, 'price_per_unit': price_per_unit}

    def calculate_total_price(self):
        total_price = 0
        for item_info in self.__items.values():
            total_price += item_info['quantity'] * item_info['price_per_unit']
        return total_price
cart = ShoppingCart()


cart.add_item("Яблука", 3, 10)
cart.add_item("Молоко", 1, 20)
cart.add_item("Хліб", 2, 15)


total_price = cart.calculate_total_price()
print("Загальна вартість покупок:", total_price)

#Завдання 3
#Створіть клас "Електронний Гаманець" додавши
#можливість видаляти та додавати гроші, а також перевіряти
#баланс.
class ElectronicWallet:
    def __init__(self):
        self.__balance = 0  # початковий баланс

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Додано {amount} грн. Новий баланс: {self.__balance} грн.")
        else:
            print("Неприпустима сума для додавання.")

    def remove_money(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято {amount} грн. Новий баланс: {self.__balance} грн.")
        else:
            print("Неприпустима сума для зняття або недостатньо коштів на рахунку.")

    def check_balance(self):
        print(f"Поточний баланс: {self.__balance} грн.")

wallet = ElectronicWallet()

wallet.add_money(100)
wallet.add_money(50)

wallet.remove_money(30)

wallet.check_balance()

#Завдання 4
#Створіть клас "Комп'ютер", який має зберігати
#інформацію про процесор, ОЗУ та відеокарту. Застосуйте
#інкапсуляцію для захисту цих даних від змін.

class Computer:
    def __init__(self, processor, ram, gpu):
        self.__processor = processor
        self.__ram = ram
        self.__gpu = gpu

    def get_processor(self):
        return self.__processor

    def get_ram(self):
        return self.__ram

    def get_gpu(self):
        return self.__gpu

    def display_info(self):
        print("Інформація про комп'ютер:")
        print(f"Процесор: {self.__processor}")
        print(f"ОЗУ: {self.__ram}")
        print(f"Відеокарта: {self.__gpu}")

my_computer = Computer("Intel Core i7", "16 ГБ", "NVIDIA GeForce RTX 3060")
my_computer.display_info()





